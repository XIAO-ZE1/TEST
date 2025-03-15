def str_reverse(s):
    """
    Reverse a string
    """
    return s[::-1]
def substr(s,x,y):
    """
    Returns the substring of s from x to y
    """
    return s[x:y]

if __name__ == "__main__":
    print(str_reverse("Hello"))
    print(substr("Hello",1,3))