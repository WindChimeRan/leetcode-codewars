-- https://www.codewars.com/kata/flatten-and-sort-an-array/train/haskell
module FlatSort where
import Data.List

flatSort :: [[Int]] -> [Int]
flatSort = sort . (=<<) id
