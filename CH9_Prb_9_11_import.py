# code for problem (import):
from CH9_Prb_9_11_module import User,Admin

admin = Admin('Kingkor', 'Karmoker', '28-06-2003', 'Student')
admin.privileges.privileges = ["can add post", "can ban user"]
admin.privileges.show_privileges()
