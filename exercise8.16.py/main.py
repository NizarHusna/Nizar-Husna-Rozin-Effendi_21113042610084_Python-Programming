# Cara 1
import function
function.greet_user()

# Cara 2
from function import greet_user
greet_user()

# Cara 3
from function import greet_user as fn
fn()

# Cara 4
import function as mn
mn.greet_user()

# Cara 5
from function import *
greet_user()