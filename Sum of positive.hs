-- https://www.codewars.com/kata/sum-of-positive/train/haskell
-- 1
module Codewars.Arrays where

positiveSum :: [Int] -> Int
positiveSum = sum . filter (>0)
