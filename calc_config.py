options = {
    "frozen": {
        "length": 4,
        "yticks": [70, 55, 40, 25],
        "ylabels": ["Frozen egg purchase", "Egg shipping", "Embryo creation", "Embryo testing"],
        "bars": [(0, 28),
                 (28, 7),
                 (35, 7),
                 (42, 7)],
        "colors": ["tab:orange",
                   "tab:orange",
                   "tab:orange",
                   "tab:blue"]

    },
    "fresh": {
        "length": 5,
        "yticks": [70, 55, 40, 25, 10],
        "ylabels": ["Egg donor match", "ED Screening", "ED Legal contracting",
                    "Egg retrieval", "Embryo creation"],
        "bars": [(0, 72),
                 (72, 56),
                 (128, 21),
                 (149, 28),
                 (177, 7)
                 ],
        "colors": ["tab:pink",
                   "tab:pink",
                   "tab:pink",
                   "tab:pink",
                   "tab:blue"]


    },

}

# base calculations for frozen eggs
calculations = {
    "frozen": {
        "time": [12, 2, 1, 4, 0, 0, 0, 1, 1, 0, 48, 6, 4, 3, 8, 0, 2, 0, 40, 2, 134],
        "cost": [61750, 31000, 0, 58000, 8900, 9250, 9000, 2000, 1000, 4000, 184900]
    },
    "fresh": {
        "time": [12, 2, 1, 12, 6, 2, 4, 1, 1, 0, 48, 6, 4, 3, 8, 0, 2, 0, 40, 2, 154],
        "cost": [76500, 31000, 10000, 58000, 8900, 9250, 9000, 2000, 1000, 4000, 209650]
    }
}
