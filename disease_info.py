"""
Plant Disease Information & Treatment Recommendations
Maps each of the 38 PlantVillage classes to human-readable names,
symptoms, causes, and actionable agricultural advice.
"""

DISEASE_INFO = {
    "Apple___Apple_scab": {
        "plant": "Apple",
        "condition": "Apple Scab",
        "is_healthy": False,
        "cause": "Fungal infection (Venturia inaequalis)",
        "symptoms": "Olive-green to dark brown or black velvety spots on leaves, fruit lesions, premature leaf drop.",
        "treatment": "Apply sulfur or copper-based fungicides early in the season. Captan or myclobutanil can be used during primary infection.",
        "prevention": "Rake and destroy fallen leaves in autumn, prune to maintain open canopy for air circulation, plant scab-resistant varieties."
    },
    "Apple___Black_rot": {
        "plant": "Apple",
        "condition": "Black Rot",
        "is_healthy": False,
        "cause": "Fungal infection (Botryosphaeria obtusa)",
        "symptoms": "Frogeye leaf spots (brown spots with purple borders), mummified fruits, cankers on limbs.",
        "treatment": "Prune out dead wood, twigs, and mummified fruit. Apply captan or thiophanate-methyl fungicides from silver tip to harvest.",
        "prevention": "Sanitize tools between cuts, avoid tree injury, prune infected wood at least 6-8 inches below visible symptoms."
    },
    "Apple___Cedar_apple_rust": {
        "plant": "Apple",
        "condition": "Cedar Apple Rust",
        "is_healthy": False,
        "cause": "Fungal infection (Gymnosporangium juniperi-virginianae)",
        "symptoms": "Bright yellow-orange spots on upper leaf surfaces; tube-like structures (aecia) on leaf undersides in late summer.",
        "treatment": "Apply myclobutanil or mancozeb fungicides when cedar galls start swelling and releasing spores in spring.",
        "prevention": "Remove nearby eastern red cedars or juniper hosts if possible. Select rust-resistant cultivars (e.g., Liberty, Freedom)."
    },
    "Apple___healthy": {
        "plant": "Apple",
        "condition": "Healthy Leaf",
        "is_healthy": True,
        "cause": "None (Plant is healthy)",
        "symptoms": "Vibrant green leaves, uniform texture, no spots, lesions, or wilting.",
        "treatment": "No treatment required. Maintain standard irrigation, mulching, and balanced fertilizer schedule.",
        "prevention": "Continue regular pest scouting, balanced pruning, and adequate watering without wetting foliage."
    },
    "Blueberry___healthy": {
        "plant": "Blueberry",
        "condition": "Healthy Leaf",
        "is_healthy": True,
        "cause": "None (Plant is healthy)",
        "symptoms": "Deep green foliage, robust growth, absence of leaf spots or chlorosis.",
        "treatment": "No treatment required. Ensure soil pH stays acidic (4.5 to 5.5).",
        "prevention": "Mulch with pine needles or sawdust, keep root zone moist, and monitor soil acidity."
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "plant": "Cherry",
        "condition": "Powdery Mildew",
        "is_healthy": False,
        "cause": "Fungal infection (Podosphaera clandestina)",
        "symptoms": "White powdery circular fungal patches on young leaves and twigs, leaf curling and distortion.",
        "treatment": "Spray wettable sulfur, potassium bicarbonate, or neem oil at first sign of white powder.",
        "prevention": "Ensure good sunlight penetration, avoid excessive nitrogen fertilization, avoid overhead watering."
    },
    "Cherry_(including_sour)___healthy": {
        "plant": "Cherry",
        "condition": "Healthy Leaf",
        "is_healthy": True,
        "cause": "None (Plant is healthy)",
        "symptoms": "Smooth green leaves, normal vigor, no mildew or bacterial canker symptoms.",
        "treatment": "No treatment needed. Keep trees properly watered and well-nourished.",
        "prevention": "Annual pruning for light and airflow; inspect regularly for aphids and fruit flies."
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "plant": "Corn (Maize)",
        "condition": "Cercospora Leaf Spot / Gray Leaf Spot",
        "is_healthy": False,
        "cause": "Fungal infection (Cercospora zeae-maydis)",
        "symptoms": "Rectangular, tan to gray spots bounded by leaf veins; can coalesce and cause significant blighting.",
        "treatment": "Foliar fungicides (strobilurins or triazoles) applied at or near tasseling if disease pressure is high.",
        "prevention": "Rotate crops with non-grasses, bury crop residues with tillage, use resistant corn hybrids."
    },
    "Corn_(maize)___Common_rust_": {
        "plant": "Corn (Maize)",
        "condition": "Common Rust",
        "is_healthy": False,
        "cause": "Fungal infection (Puccinia sorghi)",
        "symptoms": "Cinnamon-brown oval to elongate pustules on both upper and lower leaf surfaces.",
        "treatment": "Fungicide applications (triazole or strobilurin-based) if rust pustules appear before silking on susceptible hybrids.",
        "prevention": "Plant rust-resistant corn varieties; plant early in the season to escape peak spore dispersal."
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "plant": "Corn (Maize)",
        "condition": "Northern Leaf Blight",
        "is_healthy": False,
        "cause": "Fungal infection (Exserohilum turcicum)",
        "symptoms": "Long, elliptical grayish-green or tan lesions (cigar-shaped), often 1 to 6 inches long.",
        "treatment": "Apply labeled foliar fungicides if symptoms appear on upper canopy leaves before pollination.",
        "prevention": "Use resistant hybrids, practice 2-year crop rotation, incorporate crop debris after harvest."
    },
    "Corn_(maize)___healthy": {
        "plant": "Corn (Maize)",
        "condition": "Healthy Leaf",
        "is_healthy": True,
        "cause": "None (Plant is healthy)",
        "symptoms": "Uniform deep green leaf blades with clear veins and strong stalk development.",
        "treatment": "No treatment required. Maintain balanced nitrogen, phosphorus, and potassium inputs.",
        "prevention": "Maintain proper plant spacing and scout weekly during vegetative and reproductive stages."
    },
    "Grape___Black_rot": {
        "plant": "Grape",
        "condition": "Black Rot",
        "is_healthy": False,
        "cause": "Fungal infection (Guignardia bidwellii)",
        "symptoms": "Reddish-brown circular leaf spots with dark borders and tiny black fruiting bodies; shriveled black mummified berries.",
        "treatment": "Fungicide sprays with myclobutanil, captan, or copper starting at bud break until berry touch.",
        "prevention": "Remove mummified berries and prune infected canes during winter dormant season; open the canopy."
    },
    "Grape___Esca_(Black_Measles)": {
        "plant": "Grape",
        "condition": "Esca (Black Measles)",
        "is_healthy": False,
        "cause": "Fungal complex (Phaeomoniella chlamydospora, Phaeoacremonium aleophilum, Fomitiporia mediterranea)",
        "symptoms": "Tiger-stripe leaf discoloration (yellowing and necrosis between veins), dark spots on berry skin.",
        "treatment": "No chemical cure once established in vascular system. Protect pruning wounds with wound sealants or Trichoderma.",
        "prevention": "Prune during dry weather late in dormancy, disinfect shears, and gently remove infected vine arms."
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "plant": "Grape",
        "condition": "Leaf Blight (Isariopsis Leaf Spot)",
        "is_healthy": False,
        "cause": "Fungal infection (Pseudocercospora vitis)",
        "symptoms": "Irregular dark brown patches on foliage, yellow halos, leaf curling and early defoliation.",
        "treatment": "Copper oxychloride, mancozeb, or chlorothalonil sprays upon first noticing lesions.",
        "prevention": "Improve ventilation inside trellising, manage weed ground cover, burn or bury leaf litter."
    },
    "Grape___healthy": {
        "plant": "Grape",
        "condition": "Healthy Leaf",
        "is_healthy": True,
        "cause": "None (Plant is healthy)",
        "symptoms": "Bright green leaves, clean margins, strong vine vigor, no spot lesions.",
        "treatment": "No treatment needed. Keep canopy managed with regular hedging and shoot positioning.",
        "prevention": "Maintain balanced grapevine nutrition and avoid over-irrigation."
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "plant": "Orange / Citrus",
        "condition": "Huanglongbing (Citrus Greening)",
        "is_healthy": False,
        "cause": "Bacterium (Candidatus Liberibacter asiaticus) transmitted by Asian citrus psyllid",
        "symptoms": "Asymmetrical blotchy mottle on leaves, yellow shoots, small lopsided bitter fruits.",
        "treatment": "Currently no cure. Control psyllid vector populations with systemic insecticides and horticultural oils.",
        "prevention": "Use certified disease-free nursery stock, remove confirmed infected trees to protect neighbors, scout for psyllids."
    },
    "Peach___Bacterial_spot": {
        "plant": "Peach",
        "condition": "Bacterial Spot",
        "is_healthy": False,
        "cause": "Bacterium (Xanthomonas arboricola pv. pruni)",
        "symptoms": "Small water-soaked angular leaf spots turning reddish-purple and falling out ('shot-hole' appearance).",
        "treatment": "Apply fixed copper sprays during dormant season and oxytetracycline sprays during bloom.",
        "prevention": "Avoid planting in light sandy soils without windbreaks, plant resistant peach cultivars, avoid excess nitrogen."
    },
    "Peach___healthy": {
        "plant": "Peach",
        "condition": "Healthy Leaf",
        "is_healthy": True,
        "cause": "None (Plant is healthy)",
        "symptoms": "Lush lance-shaped green leaves without holes, curl, or spotting.",
        "treatment": "No treatment needed. Follow regular seasonal irrigation and fertilization.",
        "prevention": "Apply dormant preventive copper sprays in late fall to prevent peach leaf curl."
    },
    "Pepper,_bell___Bacterial_spot": {
        "plant": "Bell Pepper",
        "condition": "Bacterial Spot",
        "is_healthy": False,
        "cause": "Bacterium (Xanthomonas euvesicatoria)",
        "symptoms": "Small yellowish-green circular spots turning dark brown with water-soaked borders on foliage.",
        "treatment": "Apply copper bactericide combined with mancozeb. Use biological control such as Bacillus subtilis.",
        "prevention": "Use pathogen-free certified seed, avoid overhead sprinkler watering, rotate away from solanaceous crops for 2 years."
    },
    "Pepper,_bell___healthy": {
        "plant": "Bell Pepper",
        "condition": "Healthy Leaf",
        "is_healthy": True,
        "cause": "None (Plant is healthy)",
        "symptoms": "Glossy deep green leaves, sturdy stem growth, vibrant flowering and fruit set.",
        "treatment": "No treatment required. Maintain consistent watering and organic mulch.",
        "prevention": "Support plants with stakes and ensure good spacing for air circulation."
    },
    "Potato___Early_blight": {
        "plant": "Potato",
        "condition": "Early Blight",
        "is_healthy": False,
        "cause": "Fungal infection (Alternaria solani)",
        "symptoms": "Dark brown to black spots with concentric rings ('target board' pattern) primarily on older bottom leaves.",
        "treatment": "Apply copper fungicides, chlorothalonil, or mancozeb at the first sign of concentric lesions.",
        "prevention": "Ensure adequate nitrogen and potassium; practice 3-year crop rotation; use drip irrigation rather than overhead."
    },
    "Potato___Late_blight": {
        "plant": "Potato",
        "condition": "Late Blight",
        "is_healthy": False,
        "cause": "Oomycete pathogen (Phytophthora infestans)",
        "symptoms": "Large, dark water-soaked leaf lesions, white fuzzy mildew on leaf underside in humid weather, rapid collapse.",
        "treatment": "Apply systemic fungicides (e.g. metalaxyl, cymoxanil, mandipropamid) immediately upon warning or detection.",
        "prevention": "Plant certified disease-free seed tubers, eliminate cull piles, destroy volunteer potato plants."
    },
    "Potato___healthy": {
        "plant": "Potato",
        "condition": "Healthy Leaf",
        "is_healthy": True,
        "cause": "None (Plant is healthy)",
        "symptoms": "Compound dark green leaves with vigorous stem canopy and no necrotic margins.",
        "treatment": "No treatment required. Maintain steady soil moisture during tuber formation.",
        "prevention": "Hill soil properly around tubers and inspect lower leaves regularly."
    },
    "Raspberry___healthy": {
        "plant": "Raspberry",
        "condition": "Healthy Leaf",
        "is_healthy": True,
        "cause": "None (Plant is healthy)",
        "symptoms": "Textured serrated green leaves, upright vigorous canes, healthy flowering.",
        "treatment": "No treatment required.",
        "prevention": "Prune out spent floricanes after fruiting; mulch with organic matter."
    },
    "Soybean___healthy": {
        "plant": "Soybean",
        "condition": "Healthy Leaf",
        "is_healthy": True,
        "cause": "None (Plant is healthy)",
        "symptoms": "Trifoliate leaves with vibrant green coloration and smooth leaf surfaces.",
        "treatment": "No treatment required. Maintain weed control and optimal soil moisture.",
        "prevention": "Inoculate seeds with Bradyrhizobium japonicum; rotate with non-legume crops."
    },
    "Squash___Powdery_mildew": {
        "plant": "Squash",
        "condition": "Powdery Mildew",
        "is_healthy": False,
        "cause": "Fungal infection (Podosphaera xanthii)",
        "symptoms": "White talcum-powder-like dust on leaf surface and petioles, leaves yellow, turn brown and crisp.",
        "treatment": "Apply sulfur, potassium bicarbonate, neem oil, or biofungicides like Bacillus amyloliquefaciens.",
        "prevention": "Plant powdery-mildew tolerant cultivars, provide wide plant spacing for sunlight, water at root base."
    },
    "Strawberry___Leaf_scorch": {
        "plant": "Strawberry",
        "condition": "Leaf Scorch",
        "is_healthy": False,
        "cause": "Fungal infection (Diplocarpon earlianum)",
        "symptoms": "Irregular purple or brown spots on upper leaf surface, spots coalesce making the leaf look scorched/burned.",
        "treatment": "Remove severely diseased leaves. Apply copper or captan fungicides during early spring emergence.",
        "prevention": "Renovate strawberry beds after harvest, thin plants to enhance air movement, avoid overhead irrigation."
    },
    "Strawberry___healthy": {
        "plant": "Strawberry",
        "condition": "Healthy Leaf",
        "is_healthy": True,
        "cause": "None (Plant is healthy)",
        "symptoms": "Glossy green trifoliate leaves, no purple scorch or fungal leaf spots.",
        "treatment": "No treatment needed. Maintain clean straw mulch below fruit and leaves.",
        "prevention": "Avoid wetting foliage during evening watering; replace strawberry crowns every 3-4 years."
    },
    "Tomato___Bacterial_spot": {
        "plant": "Tomato",
        "condition": "Bacterial Spot",
        "is_healthy": False,
        "cause": "Bacterium (Xanthomonas spp.)",
        "symptoms": "Small, dark greasy spots with yellow halos on leaves; scabby dark lesions on green fruit.",
        "treatment": "Copper-based bactericides paired with mancozeb; bacteriphage biopesticides if available.",
        "prevention": "Sterilize stakes and cages, water at the soil level, rotate crops away from solanaceous plants."
    },
    "Tomato___Early_blight": {
        "plant": "Tomato",
        "condition": "Early Blight",
        "is_healthy": False,
        "cause": "Fungal infection (Alternaria solani)",
        "symptoms": "Brown to black spots with distinct concentric rings ('bullseye'), leaves yellow around spots and drop.",
        "treatment": "Apply copper fungicide, chlorothalonil, or biofungicides. Remove affected lower leaves.",
        "prevention": "Mulch around base to prevent soil splash, prune lower foliage 12 inches off soil, stake plants upright."
    },
    "Tomato___Late_blight": {
        "plant": "Tomato",
        "condition": "Late Blight",
        "is_healthy": False,
        "cause": "Oomycete pathogen (Phytophthora infestans)",
        "symptoms": "Large, irregular water-soaked pale green to dark brown patches, white cottony mold under leaves in damp weather.",
        "treatment": "Apply protective fungicides immediately upon warning. Destroy heavily infected plants to stop spore spread.",
        "prevention": "Avoid overhead watering, space plants adequately, grow late-blight resistant varieties (e.g. Mountain Magic)."
    },
    "Tomato___Leaf_Mold": {
        "plant": "Tomato",
        "condition": "Leaf Mold",
        "is_healthy": False,
        "cause": "Fungal infection (Passalora fulva)",
        "symptoms": "Pale greenish-yellow spots on upper leaf surfaces; olive-green velvety fungal patches on leaf undersides.",
        "treatment": "Apply copper-based fungicides or biofungicides (Bacillus subtilis). Reduce greenhouse/tunnel humidity.",
        "prevention": "Keep relative humidity below 85%, use fans and ventilation, space plants generously, water early morning."
    },
    "Tomato___Septoria_leaf_spot": {
        "plant": "Tomato",
        "condition": "Septoria Leaf Spot",
        "is_healthy": False,
        "cause": "Fungal infection (Septoria lycopersici)",
        "symptoms": "Numerous small circular spots with gray or white centers and dark brown margins, containing tiny black specks.",
        "treatment": "Apply copper fungicides or chlorothalonil at the very first sign. Strip off diseased lower leaves.",
        "prevention": "Mulch soil around base, avoid overhead sprinkler irrigation, practice crop rotation and fall garden cleanup."
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "plant": "Tomato",
        "condition": "Two-Spotted Spider Mites",
        "is_healthy": False,
        "cause": "Pest infestation (Tetranychus urticae)",
        "symptoms": "Fine stippling (tiny yellow or white speckles) on leaves, fine silky webbing on leaf undersides, bronzed leaves.",
        "treatment": "Spray insecticidal soap, neem oil, or horticultural oils covering undersides. Release predatory mites (Phytoseiulus persimilis).",
        "prevention": "Avoid hot, dusty conditions; keep plants well-watered; hose down dusty leaves with strong water spray."
    },
    "Tomato___Target_Spot": {
        "plant": "Tomato",
        "condition": "Target Spot",
        "is_healthy": False,
        "cause": "Fungal infection (Corynespora cassiicola)",
        "symptoms": "Brown pinpoint spots expanding into target-like lesions with concentric rings and yellow chlorotic halos.",
        "treatment": "Foliar fungicides such as azoxystrobin, chlorothalonil, or copper hydroxide applied before disease becomes severe.",
        "prevention": "Improve airflow in canopy, prune lower suckers, discard plant debris, avoid overhead irrigation."
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "plant": "Tomato",
        "condition": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "is_healthy": False,
        "cause": "Begomovirus transmitted by silverleaf whiteflies (Bemisia tabaci)",
        "symptoms": "Severe stunting, leaves curl upwards and turn cupped/crumpled with chlorotic yellow margins, flowers drop.",
        "treatment": "No cure for viral infection. Remove and bag infected plants immediately to stop virus reservoir.",
        "prevention": "Control whitefly vectors using yellow sticky traps, insecticidal soap, floating row covers, plant TYLCV-resistant varieties."
    },
    "Tomato___Tomato_mosaic_virus": {
        "plant": "Tomato",
        "condition": "Tomato Mosaic Virus (ToMV)",
        "is_healthy": False,
        "cause": "Tobamovirus (mechanically transmitted via hands, tools, smoking)",
        "symptoms": "Mottled light and dark green mosaic patterns on leaves, leaf distortion, 'fern-leaf' appearance, stunted plants.",
        "treatment": "No chemical cure. Remove and burn/dispose infected plants. Wash hands and tools in 20% non-fat dry milk solution.",
        "prevention": "Wash hands with soap before touching plants (especially smokers), disinfect pruners, use certified clean seed."
    },
    "Tomato___healthy": {
        "plant": "Tomato",
        "condition": "Healthy Leaf",
        "is_healthy": True,
        "cause": "None (Plant is healthy)",
        "symptoms": "Vigorous deep green leaves with strong fragrant scent, strong petioles, sturdy blossom sets.",
        "treatment": "No treatment required. Maintain regular watering, stake or cage vines, and side-dress with compost.",
        "prevention": "Mulch soil surface, prune suckers for adequate air passage, and scout weekly for pests."
    }
}


def format_class_name(raw_name: str) -> str:
    """Formats raw class name into a clean, human-readable display string."""
    return raw_name.replace("___", " - ").replace("_", " ").strip()


def get_disease_info(raw_name: str) -> dict:
    """Returns detailed condition information, symptoms, treatment and prevention advice."""
    if raw_name in DISEASE_INFO:
        return DISEASE_INFO[raw_name]
    
    # Fallback heuristic
    parts = raw_name.split("___")
    plant = parts[0].replace("_", " ").strip() if len(parts) > 0 else "Unknown Plant"
    condition = parts[1].replace("_", " ").strip() if len(parts) > 1 else "Unknown Condition"
    is_healthy = "healthy" in condition.lower()
    
    return {
        "plant": plant,
        "condition": condition,
        "is_healthy": is_healthy,
        "cause": "N/A" if is_healthy else "Pathogen infection",
        "symptoms": "No noticeable symptoms." if is_healthy else "Lesions, discoloration, or abnormal spotting on foliage.",
        "treatment": "No treatment needed." if is_healthy else "Consult local agricultural extension or apply appropriate fungicide/bactericide.",
        "prevention": "Continue standard horticultural care and regular scouting."
    }
