from llama_index.core.evaluation import FaithfulnessEvaluator
from proccess import llm, index, query_engine

evaluator = FaithfulnessEvaluator(
    llm=llm,
    index=index,
    query_engine=query_engine,
)
response = query_engine.query("What is the main idea of the document?")
eval_result = evaluator.evaluate_response(response= response)
eval_result.print_report()


