from research_agent.manager_agent import manager_agent


def run():

    print("🤖 Multi-Agent AI System")
    print("------------------------")

    while True:

        query = input("\nAsk something (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        result = manager_agent(query)

        print("\n📢 Response:\n")
        print(result)


if __name__ == "__main__":
    run()