leaf_nodes = ["bone lesion",
			  "bullas",
			  "ground glass pattern",
			  "consolidation",
			  "lobar atelectasis",
			  "laminar atelectasis",
			  "apical pleural thickening",
			  "calcified pleural thickening",
			  "pulmonary mass",
			  "nodule",
			  "adenopathy",
			  "vascular hilar enlargement",
			  "granuloma",
			  "cardiomegaly",
			  "aortic atheromatosis",
			  "descendent aortic elongation",
			  "aortic button enlargement",
			  "supra aortic elongation"
			  ]

internal_nodes = [
			  "interstitial pattern",
			  "alveolar pattern",
			  "infiltrates",
			  "atelectasis",
			  "pleural thickening",
			  "mass",
			  "hilar enlargement",
			  "aortic elongation",
			  "aortic disease",
			  "cardiac abnormality",
			  "opacity",
			  "pulmonary abnormality",
			  "pulmonary nodules and masses",
			  "abnormal"
]

disease_dict = {}
disease_dict_inv = {}
for i, disease in enumerate(leaf_nodes + internal_nodes):
	disease_dict[disease] = i
	disease_dict_inv[i] = disease

tree_structure = {
		"ground glass pattern":"interstitial pattern",
		"consolidation":"alveolar pattern",
        "interstitial pattern":"infiltrates",
        "alveolar pattern":"infiltrates",
        "lobar atelectasis":"atelectasis",
        "laminar atelectasis":"atelectasis",
        "apical pleural thickening":"pleural thickening",
        "calcified pleural thickening":"pleural thickening",
        "pulmonary mass":"mass",
        "adenopathy":"hilar enlargement",
        "vascular hilar enlargement":"hilar enlargement",
        "descendent aortic elongation":"aortic elongation",
        "aortic button enlargement":"aortic elongation",
        "supra aortic elongation":"aortic elongation",
        "aortic atheromatosis":"aortic disease",
        "aortic elongation":"aortic disease",
        "aortic disease":"cardiac abnormality",
        "cardiomegaly":"cardiac abnormality",
        "infiltrates":"opacity",
        "atelectasis":"opacity",
        "opacity":"pulmonary abnormality",
        "bullas":"pulmonary abnormality",
        "pleural thickening":"pulmonary abnormality",
        "mass":"pulmonary nodules and masses",
        "nodule":"pulmonary nodules and masses",
        "hilar enlargement":"pulmonary nodules and masses",
        "granuloma":"pulmonary nodules and masses",
        "bone lesion":"abnormal",
        "pulmonary abnormality":"abnormal",
        "pulmonary nodules and masses":"abnormal",
        "cardiac abnormality":"abnormal",
}



tree_structure_inv = {}
for i in tree_structure:
	if tree_structure[i] not in tree_structure_inv:
		tree_structure_inv[tree_structure[i]] = [i]
	else:
		tree_structure_inv[tree_structure[i]].append(i)



