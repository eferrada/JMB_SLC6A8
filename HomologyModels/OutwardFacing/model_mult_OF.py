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
            alnfile  = 'SLC6A8-mult_OF.ali',     # alignment filename
            knowns   = ('5i6zA', '5i6xA', '4xp4A', '4xp9C', '4xnxA', '4xp1A', '4xp5A', '4xphA', '4xpbA', '4xptA', '4m48A', '4xpgA', '4xnuA', '3tt1A', '3qs4A', '3f3aA'),              # codes of the templates
            sequence = 'SLC6A8')              # code of the target
a.starting_model= 101                 # index of the first model
a.ending_model  = 150                 # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do the actual comparative modeling
