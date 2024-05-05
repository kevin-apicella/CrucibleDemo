class User:
    def __init__(self):
        self.need_embryos = True
        self.need_donor_materials = False
        self.need_eggs = "fresh"  # "frozen" "fresh" "none"
        self.need_sperm = False
        self.coparenting = True
        self.international = False

    def change_embryo_state(self, input):
        self.need_embryos = input