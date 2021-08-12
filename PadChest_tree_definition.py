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

disease_dict_PLCOonly_v2 = {}
disease_dict_inv_PLCOonly_v2 = {}
for i, disease in enumerate(leaf_nodes + internal_nodes):
	disease_dict_PLCOonly_v2[disease] = i
	disease_dict_inv_PLCOonly_v2[i] = disease

tree_structure_PLCOonly_v2 = {
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



# disease_dict_PLCOonly_v2 = {
# 	"bone lesion":0,
# 	"bullas":1,
# 	"ground glass pattern":2,
# 	"consolidation":3,
# 	"lobar atelectasis":4,
# 	"laminar atelectasis":5,
# 	"apical pleural thickening":6,
# 	"calcified pleural thickening":7,
# 	"pulmonary mass":8,
# 	"nodule":9,
# 	"adenopathy":10,
# 	"vascular hilar enlargement":11,
# 	"calcified granuloma":12,
# 	"cardiomegaly":13,
# 	"aortic atheromatosis":14,
# 	"descendent aortic elongation":15,
# 	"aortic button enlargement":16,
# 	"supra aortic elongation":17,

# 	"interstitial pattern":18,
# 	"alveolar pattern":19,
# 	"aortic elongation":20,
# 	"aortic disease":21,
# 	"infiltrates":22,
# 	"atelectasis":23,
# 	"pleural thickening":24,
# 	"mass":25,
# 	"hilar enlargement":26,
# 	"granuloma":27,
# 	"cardiac abnormality":28,
# 	"opacity":29,
# 	"pulmonary abnormality":30,
# 	"pulmonary nodules and masses":31,
# 	"abnormal":32
# }
# disease_dict_inv_PLCOonly_v2 = {}
# for i in range(len(disease_dict_PLCOonly_v2)):
# 	for j in disease_dict_PLCOonly_v2:
# 		if disease_dict_PLCOonly_v2[j] == i:
# 			disease_dict_inv_PLCOonly_v2[i] = j


# tree_structure_PLCOonly_v2 = {
#         "ground glass pattern":"interstitial pattern",
#         "interstitial pattern":"infiltrates",
#         "consolidation":"alveolar pattern",
#         "alveolar pattern":"infiltrates",
#         "lobar atelectasis":"atelectasis",
#         "laminar atelectasis":"atelectasis",
#         "apical pleural thickening":"pleural thickening",
#         "calcified pleural thickening":"pleural thickening",
#         "pulmonary mass":"mass",
#         "adenopathy":"hilar enlargement",
#         "vascular hilar enlargement":"hilar enlargement",
#         "calcified granuloma":"granuloma",
#         "descendent aortic elongation":"aortic elongation",
#         "aortic button enlargement":"aortic elongation",
#         "supra aortic elongation":"aortic elongation",
#         "aortic atheromatosis":"aortic disease",
#         "aortic elongation":"aortic disease",
#         "aortic disease":"cardiac abnormality",
#         "cardiomegaly":"cardiac abnormality",
#         "infiltrates":"opacity",
#         "atelectasis":"opacity",
#         "opacity":"pulmonary abnormality",
#         "bullas":"pulmonary abnormality",
#         "pleural thickening":"pulmonary abnormality",
#         "mass":"pulmonary nodules and masses",
#         "nodule":"pulmonary nodules and masses",
#         "hilar enlargement":"pulmonary nodules and masses",
#         "granuloma":"pulmonary nodules and masses",
#         "bone lesion":"abnormal",
#         "pulmonary abnormality":"abnormal",
#         "pulmonary nodules and masses":"abnormal",
#         "cardiac abnormality":"abnormal",
# }
#parent nodes
tree_structure_inv_PLCOonly_v2 = {}
for i in tree_structure_PLCOonly_v2:
	if tree_structure_PLCOonly_v2[i] not in tree_structure_inv_PLCOonly_v2:
		tree_structure_inv_PLCOonly_v2[tree_structure_PLCOonly_v2[i]] = [i]
	else:
		tree_structure_inv_PLCOonly_v2[tree_structure_PLCOonly_v2[i]].append(i)

# for i in tree_structure_inv_PLCOonly_v2:
# 	print(i,":",tree_structure_inv_PLCOonly_v2[i])


