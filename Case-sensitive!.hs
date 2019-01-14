-- https://www.codewars.com/kata/case-sensitive-1/train/haskell
module CaseSensitive where 

import Data.Char

caseSensitive :: String -> (Bool,String)
caseSensitive xs = (all isLower xs, filter isUpper xs)
