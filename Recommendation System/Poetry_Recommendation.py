import faiss
import numpy as np
import json
import os
import pandas as pd
from llama_cpp import Llama
import ast
# from transformers import pipeline

global csv_path, model_path, recommendations, results, author, title, text
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(THIS_FOLDER, 'all-MiniLM-L6-v2-Q8_0.gguf')
csv_path = os.path.join(THIS_FOLDER, 'Tang Poetry Dataset.csv')
recommendations = []
results = []
author, title, text =[],[],[]
print(f"模型路徑: {model_path}")
print(f"cccccCSV 文件路徑: {csv_path}")
class PoetryRecommender:
    global csv_path, model_path
    def __init__(self, model_path,csv_path, index_path="faiss_index.bin", mapping_path="poetry_mapping.json"): 
        self.model_path = model_path
        self.dimension = 384  # 嵌入向量的維度
        self.index_path = os.path.join(THIS_FOLDER, index_path)  # 索引檔案路徑
        self.mapping_path = os.path.join(THIS_FOLDER, mapping_path)  # 對應文字檔檔案路徑
        self.csv_path = csv_path  # 使用修正後的 CSV 文件路徑
        print(f"CSV 文件路徑: {csv_path}")
        # 初始化 FAISS 索引(維度為 384)使用IndexFlatL2，用於計算L2距離來比對相似度
        self.index = faiss.IndexFlatL2(self.dimension)
        self.poetry_mapping = {}  # 對應文件字典
        # 初始化 Llama 模型
        print(f"模型路徑: {self.model_path}")
        self.llama = Llama(model_path=self.model_path, embedding=True)
        
        # 載入索引和對應的文件
        self.load_index()
        self.load_mapping()
        self.check_file()
    
    def check_file(self):
        """檢查索引和映射文件是否存在，如果不存在則重新生成"""
        index_exists = os.path.exists(self.index_path)
        mapping_exists = os.path.exists(self.mapping_path)

        if not index_exists or not mapping_exists:
            print("索引或映射文件不存在，從 CSV 文件生成資料...")
            self.add_poetry_from_csv(self.csv_path)
        else:
            print("索引和映射文件已存在，跳過 CSV 加載。")
            self.load_index()
            self.load_mapping()
    def save_index(self):
        """保存 FAISS 索引"""
        try:
            faiss.write_index(self.index, self.index_path)
            print(f"成功保存索引到 {self.index_path}")
        except Exception as e:
            print(f"保存索引失敗: {e}")

    def load_index(self):
        """加載 FAISS 索引"""
        if os.path.exists(self.index_path):
            try:
                self.index = faiss.read_index(self.index_path)
                print(f"成功加載索引，索引項目數量: {self.index.ntotal}")
            except Exception as e:
                print(f"加載索引失敗: {e}")
        else:
            print("索引文件不存在。")

    def save_mapping(self):
        """保存詩文映射"""
        try:
            with open(self.mapping_path, "w", encoding="utf-8") as f:
                json.dump(self.poetry_mapping, f, ensure_ascii=False, indent=4)
            print(f"成功保存映射到 {self.mapping_path}")
        except Exception as e:
            print(f"保存映射失敗: {e}")

    def load_mapping(self):
        """加載詩文映射"""
        if os.path.exists(self.mapping_path):
            try:
                with open(self.mapping_path, "r", encoding="utf-8") as f:
                    self.poetry_mapping = json.load(f)
                print(f"成功加載詩文映射，映射長度: {len(self.poetry_mapping)}")
            except Exception as e:
                print(f"加載映射失敗: {e}")
        else:
            print("詩文映射文件不存在。")

    def add_poetry(self, poetry_id, text, title, author):
        """將詩文添加到索引"""
        print("ttttt", text)
        try:
            embedding = self.get_embedding(text)
            if embedding is not None:
                # 添加嵌入到 FAISS 索引
                self.index.add(np.array([embedding]))
                # 添加詩文到映射
                self.poetry_mapping[str(self.index.ntotal - 1)] = {
                    "id": poetry_id,
                    "title": title,
                    "author": author,
                    "text": text,
                }
                print(f"映射長度: {len(self.poetry_mapping)}")
                # 保存索引和映射
                self.save_index()
                self.save_mapping()
                
                print(f"成功添加詩文到索引，詩文 ID: {poetry_id}")
            else:
                print(f"無法生成嵌入，詩文 ID: {poetry_id}")
        except Exception as e:
            print(f"添加詩文失敗: {e}")

    def add_poetry_from_csv(self, csv_path, batch_size=10):
        """從 CSV 文件中批量添加詩文到索引"""
        try:
            data = pd.read_csv(csv_path)
            for start in range(0, len(data), batch_size):
                batch = data.iloc[start:start + batch_size]
                for _, row in batch.iterrows():
                    try:
                        poetry_id = row['ID']
                        text = row['Poem Text']
                        title = row['Poem Title']
                        author = row['Author']
                        self.add_poetry(poetry_id, text, title, author)
                    except Exception as e:
                        print(f"處理失敗: {row}, 原因: {e}")
        except Exception as e:
            print(f"從 CSV 加載詩文失敗: {e}")
    def get_embedding(self, text):
        """為文本生成嵌入"""
        try:
            text = text.replace("\n", " ")  # 去除文本中的換行符
            response = self.llama.embed(text)  # 使用 llama_cpp 生成嵌入
    
            if isinstance(response, dict):
                if 'embedding' in response:
                    embedding = response['embedding']
                    return np.array(embedding, dtype="float32")
                else:
                    print(f"嵌入回應中沒有 'embedding' 鍵: {response}")
                    raise Exception("嵌入回應格式錯誤或無數據可用")
            elif isinstance(response, list):
                # 如果 response 是列表，直接返回嵌入
                return np.array(response, dtype="float32")
            else:
                print(f"嵌入回應不是字典或列表類型: {response}")
                raise Exception("嵌入回應格式錯誤或無數據可用")
        except Exception as e:
            print(f"嵌入生成失敗，詳細錯誤：{e}")
            raise Exception(f"嵌入生成失敗: {e}")
            

    def recommend_poetry(self, query_text, top_n=5):
        """基於輸入的查詢文本推薦相關的詩文"""
        try:
            query_embedding = self.get_embedding(query_text)
            print(f"查詢嵌入向量形狀: {query_embedding.shape}")
        
            if self.index.ntotal == 0:
                print("FAISS 索引為空，無法進行推薦。")
                return []
        
            print(f"FAISS 索引總數: {self.index.ntotal}, 詩文映射長度: {len(self.poetry_mapping)}")
            # 使用 FAISS 進行搜索
            distances, indices = self.index.search(np.array([query_embedding]), top_n)
            print(f" Distances: {distances},Indices: {indices}")

            global recommendations
            recommendations = []
            for idx, dist in zip(indices[0], distances[0]):
                poetry_data = self.poetry_mapping.get(str(idx))  # 使用字符串索引查找映射
                if poetry_data:  # 確保映射存在
                    recommendations.append({
                        "poetry": poetry_data,
                        "distance": dist,
                    })
                    print(f"推薦數量: {len(recommendations)}")
                    print(f"推薦詩文: {recommendations}")
                else:
                    print(f"詩文映射不存在，索引: {idx}, 映射長度: {len(self.poetry_mapping)}")  # 打印對應的索引
                    print(f"詩文映射錯誤，請檢查索引: {idx} 在映射文件中的對應情況")
                    
                    # 嘗試重新加載映射文件
                    self.load_mapping()

                    # 再次檢查詩文映射
                    poetry_data = self.poetry_mapping.get(str(idx))
                    if poetry_data:
                        recommendations.append({
                            "poetry": poetry_data,
                            "distance": dist,
                        })
                    else:
                        print(f"仍然無法找到詩文映射，索引: {idx}")
            
            return recommendations
        except Exception as e:
            print(f"推薦失敗，原因：{e}")
            return []

class User:
    def __init__(self, recommender):
        self.recommender = recommender
        self.tags = []  # 預設標籤
        # self.explanation_model = pipeline("text-generation", model="gpt2")  # 使用 GPT-2 模型生成解釋
    # 選擇標籤
    def select_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)
            print(f"已選擇標籤: {tag}")
        else:
            print(f"標籤 {tag} 已經選擇過了")
    
    def clear_tags(self):
        self.tags = []
        print("已清除所有標籤")

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)
            print(f"已移除標籤: {tag}")
        else:
            print(f"標籤 {tag} 不在已選擇的標籤中")
    
    def recommend_poetry(self, query_text, top_n=5):
        query_text = " ".join(self.tags) + " " + query_text
        print(f"查詢文本: {query_text}")
        global results, author, title, text
        results = self.recommender.recommend_poetry(query_text=query_text, top_n=top_n)
        author, title, text=self.display_recommendations(results, query_text)
        print("1235555555555",author, title, text)
        return author, title, text
    # def explain_recommendation(self, query_text, poetry_text, similarity_score):
    #     """
    #     生成推薦結果的解釋。
    #     """
    #     try:
    #         explanation_prompt ="""
    #         查詢文本：{query_text}\n
    #             推薦詩文：{poetry_text}\n
    #             相似度分數：{similarity_score}\n\n
    #             請解釋為什麼這首詩與查詢文本相關，並指出具體的語義或主題相似之處。"""
            
    #         explanation = self.explanation_model(
    #             messages = [
    #             {"role": "system", "content":  explanation_prompt}, 
              
    #         ], 
    #             truncation=True,  # 啟用截斷
    #             max_new_tokens=100  # 設置 max_new_tokens
    #         )[0]['generated_text']
    #         return explanation
    #     except Exception as e:
    #         print(f"生成推薦解釋失敗: {e}")
    #         return "無法生成推薦解釋。"

    def display_recommendations(self, results, query_text):
        global author, title, text
        author = [""] * 5
        title = [""] * 5
        text = [""] * 5
        for i, result in enumerate(results):
            poetry_data = result['poetry']
            author[i] = poetry_data['author'] if pd.notna(poetry_data['author']) else "佚名"
            title[i] = poetry_data['title']
            text[i] = poetry_data['text']
            similarity_score = result['distance']
            
            # 打印推荐结果
            print(f"推薦詩文: {author[-1]}--{title[-1]}。內容：{text[-1]}, 相似度: {similarity_score}")

            # # 生成並顯示解釋
            # explanation = self.explain_recommendation(query_text, text, similarity_score)
            # print(f"解釋：{explanation}")
        
        # 清空用戶標籤
        self.clear_tags()
        print("DDDDDDDd",author, title, text)
        return author, title, text

if __name__ == "__main__":
    # 初始化---1
    recommender = PoetryRecommender(model_path, csv_path)
    user = User(recommender)
    
    # 選擇標籤---2
    user.select_tag("抒情")
    user.select_tag("思鄉")
    
    query = "離別" #可以是空的
    print(f"查詢文本：{query}")

    # 用戶推薦詩歌---3
    user.recommend_poetry(query)
    # print(recommendations)
    # print(results)
    print(author, title, text)