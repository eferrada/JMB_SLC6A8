# Illustrates the SALIGN multiple structure/sequence alignment

from modeller import *

log.verbose()
env = Environ()
env.io.atom_files_directory = ['../TEMPLATEs/', '../atom_files/']

aln = Alignment(env)
for (code, chain) in (('5i6z', 'A'), ('5i6x', 'A'), ('4xp4', 'A'), ('4xp9', 'C'), ('4xnx', 'A'), ('4xp1', 'A'), ('4xp5', 'A'), ('4xph', 'A'), ('4xpb', 'A'), ('4xpt', 'A'), ('4m48', 'A'), ('4xpg', 'A'), ('4xnu', 'A'), ('3tt1', 'A'), ('3qs4', 'A'), ('3f3a', 'A')):
    mdl = Model(env, file=code, model_segment=('FIRST:'+chain, 'LAST:'+chain))
    aln.append_model(mdl, atom_files=code, align_codes=code+chain)

for (weights, write_fit, whole) in (((1., 0., 0., 0., 1., 0.), False, True),
                                    ((1., 0.5, 1., 1., 1., 0.), False, True),
                                    ((1., 1., 1., 1., 1., 0.), True, False),
                                    ((1., 0., 0., 0., 1., 0.), False, True),
                                    ((1., 0.5, 1., 1., 1., 0.), False, True),
                                    ((1., 1., 1., 1., 1., 0.), True, False),
                                    ((1., 0., 0., 0., 1., 0.), False, True),
                                    ((1., 0., 0., 0., 1., 0.), False, True),
                                    ((1., 0.5, 1., 1., 1., 0.), False, True),
                                    ((1., 1., 1., 1., 1., 0.), True, False),
                                    ((1., 0., 0., 0., 1., 0.), False, True),
                                    ((1., 0.5, 1., 1., 1., 0.), False, True),
                                    ((1., 1., 1., 1., 1., 0.), True, False),
                                    ((1., 0., 0., 0., 1., 0.), False, True),
                                    ((1., 0., 0., 0., 1., 0.), False, True),
                                    ((1., 0.5, 1., 1., 1., 0.), False, True)):
    aln.salign(rms_cutoff=3.5, normalize_pp_scores=False,
               rr_file='$(LIB)/as1.sim.mat', overhang=30,
               gap_penalties_1d=(-450, -50),
               gap_penalties_3d=(0, 3), gap_gap_score=0, gap_residue_score=0,
               dendrogram_file='s6a8_salign.tree',
               alignment_type='tree', # If 'progresive', the tree is not
                                      # computed and all structues will be
                                      # aligned sequentially to the first
               feature_weights=weights, # For a multiple sequence alignment only
                                        # the first feature needs to be non-zero
               improve_alignment=True, fit=True, write_fit=write_fit,
               write_whole_pdb=whole, output='ALIGNMENT QUALITY')

aln.write(file='s6a8_salign_OF.pap', alignment_format='PAP')
aln.write(file='s6a8_salign_OF.ali', alignment_format='PIR')

aln.salign(rms_cutoff=1.0, normalize_pp_scores=False,
           rr_file='$(LIB)/as1.sim.mat', overhang=30,
           gap_penalties_1d=(-450, -50), gap_penalties_3d=(0, 3),
           gap_gap_score=0, gap_residue_score=0, dendrogram_file='s6a8_salign_OF.tree',
           alignment_type='progressive', feature_weights=[0]*6,
           improve_alignment=False, fit=False, write_fit=True,
           write_whole_pdb=False, output='QUALITY')

