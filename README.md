# code_test
Code test

Attached there is a simple python tool and a VCF file. It works like:

 
```bash
python3.11 read_vcf.py mock.vcf

Zygosity breakdown for 32 variants with depth > 10:

0/0: 6
0/1: 8
1/0: 8
1/1: 10


python3.11 read_vcf.py mock.vcf --depth 44

Zygosity breakdown for 22 variants with depth > 44:

0/0: 4
0/1: 3
1/0: 6
1/1: 9
```


Here are 10 different options that could be useful to enhance the functionality of this VCF parsing command-line tool:

 

1. `--sample`: Specify the samples of interest. For example, `--sample SAMPLE2` would only count variants in sample 2.

2. `--allele-frequency`: Specify an allele frequency threshold for considering variants. For instance, `--allele-frequency 0.05` would only count variants with an allele frequency greater than 0.05.

3. `--chromosome`: Filter variants based on a specific chromosome. For example, `--chromosome 1` would only process variants on chromosome 1.

4. `--position-range`: Specify a range of positions to focus on. For instance, `--position-range 1000-5000` would only consider variants with positions between 1000 and 5000.

5. `--include-filter`: Include variants with specific filter flags. For example, `--include-filter PASS` would only count variants marked as "PASS" in the FILTER column (need to make this col).

6. `--exclude-filter`: Exclude variants with specific filter flags. For instance, `--exclude-filter LowQual` would exclude variants marked as "LowQual" in the FILTER column.

7. `--include-info`: Include additional INFO fields in the output. For example, `--include-info DP` would display the "DP" INFO field along with other variant information.

8. `--output-format`: Specify the output format for the parsed data, such as CSV or JSON.

9. `--output-file`: Save the parsed data to a specified output file instead of printing it to the console.

10. `--verbose`: Enable verbose mode to display detailed progress and additional information during the parsing process.

 

Your task is to add all 10 options, fix the current bug and refactor the code to use pandas to read, write and filter data. Extra marks for clean code https://github.com/zedr/clean-code-python and type hints. There's no right answer, be creative and showcase your knowledge of Python as much as is reasonable. Unit tests are not required but feel free to add if you want. Docker is also optional.
