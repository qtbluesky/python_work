#import printing_models
#from printing_models import print_models,show_completed_models
#from printing_models import print_models as pm, show_completed_models as scm
import printing_models as pm

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#printing_models.print_models(unprinted_designs[:], completed_models)
#printing_models.show_completed_models(completed_models)

#pm(unprinted_designs[:], completed_models)
#scm(completed_models)

pm.print_models(unprinted_designs[:], completed_models)
pm.show_completed_models(completed_models)
