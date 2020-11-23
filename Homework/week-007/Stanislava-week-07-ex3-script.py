def fn(lst):
    with open("output.html", "w") as filename:
        filename.write('<body>\n')
        filename.write(" ".join(lst[1:]))
        filename.write('\n</body>')

if __name__ == "__main__":
    import sys
    fn(sys.argv)
    
    #print(" ".join(sys.argv[1:]))  #other option