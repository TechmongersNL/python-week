import functions

def test_double():
  assert functions.double(2) == 4
  assert functions.double(0) == 0
  assert functions.double(-42) == -84

def test_double_first():
  assert functions.double_first(1, 2) == 2
  assert functions.double_first(34, 7) == 68

def test_big_double():
  assert functions.big_double(10, 8) == 20
  assert functions.big_double(67, 84) == 168

def test_repeat():
  assert functions.repeat("python", 3) == "pythonpythonpython"
  assert functions.repeat("hi", 5) == "hihihihihi"
  assert functions.repeat("hi", -1) == ""

def test_batman():
  assert functions.batman() == "nananananananananana batman!"

def test_max():
  assert functions.maxi(10, 5) == 10
  assert functions.maxi(-10, 50) == 50
  assert functions.maxi(-5, -50) == - 5

def test_max_divide():
  assert functions.max_divide(10, 5) == 0.5
  assert functions.max_divide(28, 7) == 0.25

def test_max_string():
  assert functions.max_string("python", "java") == "python"
  assert functions.max_string("code", "sleep") == "sleep"
  assert functions.max_string("aa", "bb") == "aa"

def test_even():
  assert functions.even(10) == True
  assert functions.even(3) == False
  assert functions.even(-5) == False

def test_even_below():
  assert functions.even_below(10) == [0, 2, 4, 6, 8]
  assert functions.even_below(-10) == []

def test_even_in():
  assert functions.even_in([0, 2, 4, 6, 8, 10]) == [0, 2, 4, 6, 8, 10]
  assert functions.even_in([0, 1, 2, 3, 4, 5]) == [0, 2, 4]
  assert functions.even_in([1, 3, 5, 7]) == []

def test_multiply_list():
  assert functions.multiply_list([2, 3, 6]) == 36
  assert functions.multiply_list([5]) == 5
  assert functions.multiply_list([10, 321, 15]) == 48150

def test_divide_array():
  assert functions.divide_array([7 , 0, 8]) == 0
  assert functions.divide_array([9]) == 9
  assert functions.divide_array([60, 2, 5, 3]) == 2

def test_average():
  assert functions.average([2, 3, 4]) == 3
  assert functions.average([2]) == 2
  assert functions.average([100, 50]) == 75

# STEVEN

def test_sum_product():
    assert functions.sum_product([1,2,3,4]) == 40
    assert functions.sum_product([0,2,4,6,8,10]) == 180

def test_uppercase_string():
    assert functions.uppercase_string("my name is steven") == "My name Is steven"
    assert functions.uppercase_string("asdfjk; tech mongers") == "Asdfjk; tech Mongers"
    assert functions.uppercase_string("There can be no better function than this one") == "There can Be no Better function Than this One"

# VIKTORIA

def test_alphabet():
    assert functions.alphabet("A") == 1
    assert functions.alphabet("e") == 5
    assert functions.alphabet("Q") == 17

def test_letter_count():
   assert functions.letter_count("Either I zip down, or he zips up, and that is a mighty long zipper on Mother's Cher jumpsuit. There are dozens of us! DOZENS! He also said some things African American-y wasn't ready to hear. Do you guys know where I could get one of those gold necklaces with the T on it? That's a cross. Across from where? So you take your mom to work every day? Bummer. Moms are such a pain in the ass, huh? It's, like, die already! I think that's one of Mom's little fibs, you know, like I'll sacrifice anything for my children. Oh, hi, Mom. I have the afternoon free. Really? Did nothing cancel?", 1) == 32
   assert functions.letter_count("Either I zip down, or he zips up, and that is a mighty long zipper on Mother's Cher jumpsuit. There are dozens of us! DOZENS! He also said some things African American-y wasn't ready to hear. Do you guys know where I could get one of those gold necklaces with the T on it? That's a cross. Across from where? So you take your mom to work every day? Bummer. Moms are such a pain in the ass, huh? It's, like, die already! I think that's one of Mom's little fibs, you know, like I'll sacrifice anything for my children. Oh, hi, Mom. I have the afternoon free. Really? Did nothing cancel?", 26) == 5
   assert functions.letter_count("Either I zip down, or he zips up, and that is a mighty long zipper on Mother's Cher jumpsuit. There are dozens of us! DOZENS! He also said some things African American-y wasn't ready to hear. Do you guys know where I could get one of those gold necklaces with the T on it? That's a cross. Across from where? So you take your mom to work every day? Bummer. Moms are such a pain in the ass, huh? It's, like, die already! I think that's one of Mom's little fibs, you know, like I'll sacrifice anything for my children. Oh, hi, Mom. I have the afternoon free. Really? Did nothing cancel?", 18) == 28
