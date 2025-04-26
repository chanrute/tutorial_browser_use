import asyncio
import logging
from langchain_openai import ChatOpenAI
from browser_use import Agent  # browser_use.py に Agent クラスが含まれていると仮定します

# ロギングの設定
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def main():
    agent = Agent(
        task="""
あなたはウェブサイトから特定の情報を抽出するエージェントです。
以下の手順を実行してください。
1. URL 'https://www.nenkin.go.jp/service/kounen/jigyosho/jigyoshokensaku.html' を開いてください。
2. 上部にある「事業所検索システム」というボタンを探してクリックしてください。
3. 検索画面が表示されたら、'事業所名称（全角）' というラベルがついた入力フィールドを探し、'スマートラウンド' と入力してください。
4. '検索実行' というテキストのボタンを探してクリックしてください。
5. クリック後、7秒間待機してください。
6. 検索結果として表示される表を探してください。
7. その表の最初のデータ行（ヘッダー行を除く1行目）にある '被保険者数' という列の値を取得してください。
8. 取得した値を半角数字に変換し、loggerを使ってINFOレベルでログに出力してください。出力形式は "🎉被保険者数: {取得した数値}" としてください。
""",
        llm=ChatOpenAI(model="gpt-4o"), # main.py と同じモデルを使用
    )

    # エージェントを実行
    await agent.run()
    logger.info("エージェントの実行が完了しました。")

if __name__ == "__main__":
    asyncio.run(main())
