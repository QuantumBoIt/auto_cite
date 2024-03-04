import requests
from bs4 import BeautifulSoup
# import pyperclip as pc

# paper = pc.paste()

paper_titles = [
    # "Federated learning: Strategies for improving communication efficiency",
    # "Deep leakage from gradients",
    # "iDLG: Improved deep leakage from gradients",
    # "Inverting gradients - how easy is it to break privacy in federated learning?",
    # "Deep models under the GAN: information leakage from collaborative deep learning",
    # "Model inversion attacks that exploit confidence information and basic countermeasures",
    # "Updates-leak: Data set inference and reconstruction attacks in online learning",
    # "Beyond inferring class representatives: User-level privacy leakage from federated learning",
    # "Mean square error of prediction as a criterion for selecting variables",
    # "A framework for evaluating gradient leakage attacks in federated learning",
    # "See through gradients: Image batch recovery via gradinversion",
    # "Federated learning: Challenges, methods, and future directions",
    # # "基于遗传算法的联邦学习优化策略的研究",
    # "Developing and validating a survival prediction model for NSCLC patients through distributed learning across 3 countries",
    # "Communication-efficient learning of deep networks from decentralized data",
    # "A review of applications in federated learning",
    # "Applications of federated learning in smart cities: recent advances, taxonomy, and open challenges",
    # "Advances and open problems in federated learning",
    # "Hhhfl: Hierarchical heterogeneous horizontal federated learning for electroencephalography",
    # "A communication efficient collaborative learning framework for distributed features",
    # "Improved reconstruction attacks on encrypted data using range query leakage",
    # "A stochastic approximation method",
    # "Adam: A method for stochastic optimization",
    # "Practical methods of optimization",
    # "On information and sufficiency",
    # "Lightgbm: A highly efficient gradient boosting decision tree",
    # "A communication-efficient parallel algorithm for decision tree",
    # "On the difficulty of training recurrent neural networks",
    # "A tail-index analysis of stochastic gradient noise in deep neural networks",
    # "Multiparty unconditionally secure protocols",
    # "Calibrating noise to sensitivity in private data analysis"
]

def get_cite(paper):

    base_url = "https://scholar.google.de/scholar?hl=de&as_sdt=0%2C5&q=" + paper + "&btnG= "

    googleSearch = requests.request("GET", url=base_url)

    bs_page = BeautifulSoup(googleSearch.content, "html.parser")
    block = bs_page.find("div", {"class": "gs_ri"})
    title = block.find("h3")
    link = title.find("a")
    citation_id = link["id"]
    
    if title is None:
        Exception("title is null")

    cite_url = "https://scholar.google.de/scholar?hl=de&q=info:" + citation_id + ":scholar.google.com/&output=cite&scirp=0"

    findLatex = requests.request("GET", url=cite_url)

    citation_view = BeautifulSoup(findLatex.content, "html.parser")
    latex_link = citation_view.find("div", {"id": "gs_citi"})

    latex_mf = latex_link.findChildren("a")[0]["href"]

    result = BeautifulSoup(requests.request("GET", url=latex_mf).content, "html.parser")
    citation = result.text
    # pc.copy(citation)
    # print("^"*20)
    # print(citation)
    # print("v"*20)
    return citation

for title in paper_titles:
    bibtex = get_cite(title)
    if bibtex:
        print(bibtex)
        print("")
        # print('-' * 20)
        # print(f"BibTeX for '{title}':\n{bibtex}")
        # print("=" * 20)
    else:
        print("ERROR" * 10)