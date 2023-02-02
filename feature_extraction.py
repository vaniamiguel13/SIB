from Bio.SeqUtils.ProtParam import ProteinAnalysis
from propy.PyPro import GetProDes
from tqdm.notebook import tqdm
import numpy as np
import pandas as pd


### DESCRIPTORS ###

# sequence lenght (1 feature)
def get_length(protein: str) -> dict:
    return {"SeqLength": len(protein)}

# aminoacid composition (20 features)
def get_aminoacid_composition(protein: str) -> dict:
    return GetProDes(protein).GetAAComp()

# dipeptide composition (400 features)
def get_dipeptide_composition(protein: str) -> dict:
    return GetProDes(protein).GetDPComp()

# tripeptide composition (8000 features)
def get_tripeptide_composition(protein: str) -> dict:
    return GetProDes(protein).GetTPComp()

# ctd descriptors (147 features)
def get_ctd_descriptors(protein: str) -> dict:
    return GetProDes(protein).GetCTD()

# molecular weight (1 feature)
def get_molecular_weight(protein: str) -> dict:
    X = ProteinAnalysis(protein)
    return {"MolecularWeight": X.molecular_weight()}

# aromaticity (1 feature)
def get_aromaticity(protein: str) -> dict:
    X = ProteinAnalysis(protein)
    return {"Aromaticity": X.aromaticity()}

# instability index (1 feature)
def get_instability_index(protein: str) -> dict:
    X = ProteinAnalysis(protein)
    return {"InstabilityIndex": X.instability_index()}

# isoelectric point (1 feature)
def get_isoelectric_point(protein: str) -> dict:
    X = ProteinAnalysis(protein)
    return {"IsoelectricPoint": X.isoelectric_point()}

# secondary structure fraction (3 features)
def get_secondary_structure_fraction(protein: str) -> dict:
    X = ProteinAnalysis(protein)
    helix, turn, sheet = X.secondary_structure_fraction()
    return {"HelixSSF": helix, "TurnSSF": turn, "SheetSSF": sheet}

# molar extinction coefficient (2 features)
def get_molar_extinction_coefficient(protein: str) -> dict:
    X = ProteinAnalysis(protein)
    reduced, oxidized = X.molar_extinction_coefficient()
    return {"ReducedMEC": reduced, "OxidizedMEC": oxidized}

# geary autocorrelation descriptors (240 features)
def get_geary_autocorrelation_descriptors(protein: str) -> dict:
    return GetProDes(protein).GetGearyAuto()

# moran autocorrelation descriptors (240 features)
def get_moran_autocorrelation_descriptors(protein: str) -> dict:
    return GetProDes(protein).GetMoranAuto()

# moreau-broto autocorrelation descriptors (240 features)
def get_moreau_broto_autocorrelation_descriptors(protein: str) -> dict:
    return GetProDes(protein).GetMoreauBrotoAuto()




### ALL DESCRIPTORS ###

# compute all descriptors (9297 features)
def get_dataset_with_features(dataset: pd.DataFrame) -> pd.DataFrame:
    # get protein sequences from dataset and initialize an empty protein_features list
    proteins = np.array(dataset.protein_sequence, dtype="str")
    protein_features = []
    for protein in tqdm(proteins):
        # compute features for each protein
        length = get_length(protein)
        aa_comp = get_aminoacid_composition(protein)
        dp_comp = get_dipeptide_composition(protein)
        tp_comp = get_tripeptide_composition(protein)
        ctd = get_ctd_descriptors(protein)
        mw = get_molecular_weight(protein)
        arom = get_aromaticity(protein)
        ii = get_instability_index(protein)
        iso_p = get_isoelectric_point(protein)
        ssf = get_secondary_structure_fraction(protein)
        mec = get_molar_extinction_coefficient(protein)
        geary = get_geary_autocorrelation_descriptors(protein)
        moran = get_moran_autocorrelation_descriptors(protein)
        moreau_broto = get_moreau_broto_autocorrelation_descriptors(protein)
        # merge dictionaries and add result to protein_features
        features = dict(length, **aa_comp, **dp_comp, **tp_comp,  **ctd, **mw, **arom, **ii, **iso_p, **ssf, **mec,
                        **geary, **moran, **moreau_broto)
        protein_features.append(features)
    # return pandas DataFrame with results
    features_df = pd.DataFrame(protein_features)
    features_df.insert(0, "seq_id", dataset.seq_id)
    return pd.concat([features_df, dataset.loc[:,["pH","tm"]]], axis=1) #Removeu-se, 'protein_sequence', e 'data_source'