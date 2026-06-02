from workflow import graph

result = graph.invoke(
    {
        "topic": "Artificial Intelligence in Healthcare",
        "email": ""
    }
)

print("\nWORKFLOW COMPLETED\n")

print(result)