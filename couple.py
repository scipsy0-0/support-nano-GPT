from sentence_transformers import SentenceTransformer, util


def make_context(txt_path, chunk_size=25):
    with open(txt_path, "r") as file:
        text = file.read()
    
    corpus = [p.strip() for p in text.split("\n\n") if p.strip()]

    embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    corpus_embeddings = embedder.encode_document(corpus, convert_to_tensor=True)
    return embedder, corpus_embeddings, corpus 


def get_context(question, embedder, corpus_embeddings, corpus, top_k=2):
    query_embedding = embedder.encode_query(question, convert_to_tensor=True)
    hits = util.semantic_search(
        query_embedding, corpus_embeddings, top_k=min(top_k, len(corpus))
        )[0]
    return "\n".join(corpus[hit["corpus_id"]] for hit in hits)

