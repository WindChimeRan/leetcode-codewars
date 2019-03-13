-- https://www.codewars.com/kata/arithmetic-sequence/train/haskell
module Term where

nthterm :: Int -> Int -> Int -> Int
nthterm first n c = first + n * c
