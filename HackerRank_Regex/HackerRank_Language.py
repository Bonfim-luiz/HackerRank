# https://www.hackerrank.com/challenges/hackerrank-language/problem
# HackerRank Language

import re 

regex = r'^\d+ (C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$'

n = int(input())
for _ in range(n):
  texto = input()
  if bool(re.findall(regex, texto)):
    print("VALID")
  else:
    print("INVALID")
