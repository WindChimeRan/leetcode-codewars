-- https://www.codewars.com/kata/5b39e3772ae7545f650000fc/solutions/haskell

-- 1
module RemoveDuplicateWords where 
import Data.List (nub)
removeDuplicateWords :: String -> String
removeDuplicateWords = tail' . concat . fmap (\x -> ' ':x) . nub . words 

tail' "" = ""
tail' xs = tail xs

-- 2
module RemoveDuplicateWords where 
import Data.List(nub)

removeDuplicateWords :: String -> String
removeDuplicateWords = unwords. nub. words 
