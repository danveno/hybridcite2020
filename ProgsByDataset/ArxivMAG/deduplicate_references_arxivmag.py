""" Remove duplicate references and refs which are not in the training data """

import pandas as pd
from gensim.models.doc2vec import Doc2Vec

import pandas as pd 
model = Doc2Vec.load('/home/ashwath/Programs/ArxivCS/Paper2Vec/ArxivMagd2v.dat')
df = pd.read_csv('/home/ashwath/Programs/ArxivCS/AdditionalOutputs/arxivmag_references.tsv', sep='\t')
# dup_df = df[df.duplicated()].shape is (9927,2)
dedup_df = df[~df.duplicated()]
# Remove the header this time as well.
# Keep only the papers which are in the offset2doctag doc2vec list.
inter1 = dedup_df[dedup_df.citing_mag_id.isin(model.docvecs.offset2doctag)]
inter2 = inter1[inter1.cited_mag_id.isin(model.docvecs.offset2doctag)]
#df.to_csv('/home/ashwath/Programs/MAG-CS-Paper2Vec/paperrefs_cs_en.tsv', sep='\t', index=False, header=None)

inter2.to_csv('/home/ashwath/Programs/ArxivCS/AdditionalOutputs/arxivmag_references_may1.tsv', sep='\t', index=False, header=None)

#dedup_df.to_csv('/home/ashwath/Programs/ArxivCS/AdditionalOutputs/arxivmag_references_deduplicated.tsv', sep='\t', header=False)