-- https://www.codewars.com/kata/fixed-xor/train/haskell
-- 1

module Codewars.Kata.FixedXor where

import Data.Char (digitToInt, intToDigit)
import Data.Bits (xor)

fixedXor :: String -> String -> String
fixedXor a b = map intToDigit $ zipWith xor (map digitToInt a) (map digitToInt b)

-- 2
module Codewars.Kata.FixedXor where

import Data.Char (digitToInt, intToDigit)
import Data.Bits (xor)
import Data.Function (on)

fixedXor :: String -> String -> String
fixedXor a b = map intToDigit $ on (zipWith xor) (map digitToInt) a b

-- 3
module Codewars.Kata.FixedXor where

import Data.Char
import Data.Bits
import Data.Function

fixedXor :: String -> String -> String
fixedXor = zipWith ((\x y -> intToDigit $ x `xor` y) `on` digitToInt)
