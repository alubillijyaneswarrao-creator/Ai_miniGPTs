from research_agent.research_agent import research_agent


def run():

    print("🔎 Autonomous Research Agent")
    print("-----------------------------")

    topic = input("Enter research topic: ")

    report = research_agent(topic)

    print("\n📄 Research Report\n")
    print(report)


if __name__ == "__main__":
    run()