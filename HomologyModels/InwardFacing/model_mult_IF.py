from modeller import *
from modeller.automodel import *

# Redefine the special_patches routine to include the additional disulfides
# (this routine is empty by default):
class MyModel(AutoModel):
    def special_patches(self, aln):
        # A disulfide between residues 8 and 45 in chain A:
        self.patch(residue_type='DISU', residues=(self.residues['121:A'],self.residues['130:A']))
        self.patch(residue_type='DISU', residues=(self.residues['139:A'],self.residues['149:A']))

env = Environ()
# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

a = MyModel(env,
            alnfile  = 'SLC6A8-mult_IF.ali',     # alignment filename
            knowns   = ('3tt3A', '6dzzA', '6yu5A', '6yu2A'),              # codes of the templates
            sequence = 'SLC6A8')              # code of the target
a.starting_model= 1                 # index of the first model
a.ending_model  = 100                 # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do the actual comparative modeling
