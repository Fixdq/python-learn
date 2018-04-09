#!/usr/bin/env python3
# encoding: utf-8
# by fixdq
import re

print(re.findall('\w','i168dfs*%45*&^(*^&%$^&67)(UY)GO IS67556YDf57t87df'))
print(re.findall('\W','i168dfs*%45*&^(*^&%$\t^&67)(U\rY)GO IS67\y556YDf57t87df'))
print(re.findall('\s','i168dfs*\n%45*&^(*^&%$^\t&67)(UY\b)GO IS\t67\r556YD\kf57t87df'))
print(re.findall('\S','i168dfs*%45*&^(*^&%$^&67)(UY)GO IS67556YDf57t87df'))
print(re.findall('\d','i168dfs*%45*&^(*^&%$^&67)(UY)GO IS67556YDf57t87df'))
print(re.findall('\D','i168dfs*%45*&^(*^&%$^&67)(UY)GO IS67556YDf57t87df'))
print(re.findall('\A','i168dfs*%45*&^(*^&%$^&67)(UY)GO IS67556YDf57t87df'))

print(re.findall('\n','-\n*@\t#$\t%\n^&'))
print(re.findall('\t','-\n*@\t#$\t%\n^&'))
print(re.findall('\t*','-\n*@\t#$\t%\n^&'))
print(re.findall('[\t*]','-\n*@\t#$\t%\n^&'))




print(re.findall('t.','t tg tgg tggg tggg tggg '))
print(re.findall('tg?','t tg tgg tggg tggg tggg '))
print(re.findall('tg*','t tg tgg tggg tggg tggg '))


print(re.findall('k{1,2}','ggkkoo'))
print(re.findall('o{0,2}','ggkkoo'))
print(re.findall('o.*','ggkkoooooooooo'))
print(re.findall('o.*?','ggkkoooooooooooo'))

print(re.findall('([a-zA-Z]+)_sb','8494yangli_sb  77777li_sb  asdf33yangL_sb'))