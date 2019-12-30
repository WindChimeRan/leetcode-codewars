module Codewars.Kata.Compare where
import Data.List

square :: Integer -> Integer
square x = x * x

comp :: [Integer] -> [Integer] -> Bool
comp as bs = (sort $ square <$> as) == sort bs
