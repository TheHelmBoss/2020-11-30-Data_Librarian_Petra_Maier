Shell

Steps for data cleaning 

1. step
Delete rows  without digits, remove corrupted cells IMPORTANT\t\t, remove intro ISSN: before the ISSN 

sed 's/\(^[^0-9]\+$\|IMPORTANT!\?		\|[Ii][Ss][Ss][Nn]:\? \? \?\)//g' 2020-12-04-Article_list_dirty.tsv > 2020-12-04-Article_list_ISSN-year.tsv

NOTE: there are 2 tabs after IMPORTANT (i.e. ... IMPORTANT!\?\t\t\ ...) 

2. step
Cut the unneeded columns (only ISSN and year columns are needed)

cut -d'	' -f5,12 2020-12-04-Article_list_ISSN-year.tsv > 2020-12-04-Article_list_ISSN-year_v2.tsv

NOTE: a tab as delimiter (i.e. -d'\t')

3. step
replace line ending to CRLF

sed 's/\r$//g' 2020-12-04-Article_list_ISSN-year_v2.tsv > 2020-12-04-Article_list_ISSN-year_v3.tsv

4. step
sort and unique

sort -n 2020-12-04-Article_list_ISSN-year_v3.tsv | uniq > 2020-12-04-Article_list_ISSN-year_v4.tsv

5. step
delete blank line
 
sed '/^$/d' 2020-12-04-Article_list_ISSN-year_v4.tsv > 2020-12-04-Article_list_ISSN-year_FINAL.tsv
