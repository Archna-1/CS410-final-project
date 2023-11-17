import metapy

def summarize_text(input_text, num_sentences=3):
    # Tokenize the input text
    tok = metapy.analyzers.ICUTokenizer(suppress_tags=True)
    
    # Create a unigram language model with the input text
    doc = metapy.index.Document()
    doc.content(input_text)
    
    # Create an inverted index configuration
    config_var = metapy.index.Config()
    config_var["stop-words"] = "en"  # You can customize the stop words list
    
    # Create an inverted index
    idx = metapy.index.make_inverted_index('tmp-inverted-index', config=config_var)

    # Tokenize and add the document to the index
    idx.add_document(doc)

    # Create a ranker for summarization
    ranker = metapy.index.OkapiBM25()

    # Rank the document using the BM25 ranker
    top_docs = ranker.score(idx, doc, num_results=num_sentences)

    # Get the top-ranked sentences
    sentences = metapy.analyzers.extract_sentences(tok, input_text)
    summary = [sentences[i] for i in top_docs]

    return ' '.join(summary)



if __name__ == "__main__":
    # Example usage
    input_text = """
    Ants are eusocial insects of the family Formicidae and, along with the related wasps and 
    bees, belong to the order Hymenoptera. Ants evolved from vespoid wasp ancestors in the Cretaceous 
    period. More than 13,800 of an estimated total of 22,000 species have been classified. They are e
    asily identified by their geniculate (elbowed) antennae and the distinctive node-like structure 
    that forms their slender waists.

Ants form colonies that range in size from a few dozen predatory individuals living in small 
natural cavities to highly organised colonies that may occupy large territories and consist of 
millions of individuals. Larger colonies consist of various castes of sterile, wingless females, 
most of which are workers (ergates), as well as soldiers (dinergates) and other specialised groups.
 Nearly all ant colonies also have some fertile males called "drones" and one or more fertile females 
 called "queens" (gynes). The colonies are described as superorganisms because the ants appear to
   operate as a unified entity, collectively working together to support the colony.
    """
    
    summary = summarize_text(input_text)
    
    print("Original Text:")
    print(input_text)
    print("\nSummarized Text:")
    print(summary)