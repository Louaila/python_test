from calculatrice import addition, diference, multiplication, quotient, racine_carree


def test_addition():
    assert addition(3, 2) == 5
   

def test_diference():
    assert diference(5, 3) == 2
    

def test_multiplication():
    assert multiplication(3, 2) == 6


# Tests pour la fonction quotient
def test_quotient():
    assert quotient(6, 3) == 2
    
# Tests pour la fonction racine_carree
def test_racine_carree():
    assert racine_carree(4) == 2
  