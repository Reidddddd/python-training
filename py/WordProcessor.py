import os
import re


class WordProcessor(object):
    def word_frequency(self, filepath):
        wordcount = {}
        file = open(file=filepath, mode='r', encoding='gbk')
        for word in re.split('，|。|,', file.read()):
            word = word.strip()
            if word in wordcount.keys():
                wordcount[word] += 1
            else:
                wordcount[word] = 1
        wordcount.pop('', None)
        return wordcount

    def file_frequency(self, filespath, outputDir):
        # For each file, get word's frequency and write output.
        for file in filespath:
            word_count = self.word_frequency(file)
            output_file = open(file=outputDir + "\\" + os.path.basename(file).replace(".txt", "_frequency.txt"),
                               mode='w', encoding='gbk')
            output_file.write("个数: " + str(len(word_count.keys())) + "\n")
            for each_word in word_count.keys():
                output_file.write(each_word + '\t' + str(word_count[each_word]) + '\n')
            output_file.close()

    def common_frequency(self, filespath, outputDir):
        # 1. Get word's frequency from each file
        words = []
        for filepath in filespath:
            words.append(self.word_frequency(filepath))
        # 2. Get the common words
        l = len(words)
        word_dict = words[0].keys()
        for i in range(1, l):
            word_dict = word_dict & words[i].keys()
        # 3. For each common word, get its frequency from each file
        res = {}
        for k in word_dict:
            for word in words:
                fre = res.get(k, [])
                fre.append(word[k])
                res[k] = fre
        # 4. Write output
        output_file = open(file=outputDir + "\\output.txt", mode='w', encoding='gbk')
        for common_key in res.keys():
            output_file.write(common_key + '\t' + '\t'.join(map(str, res[common_key])) + '\n')
        output_file.close()

    def calculate_frequency(self, inputDir, outputDir):
        def get_filepaths(directory):
            file_paths = []
            for root, directories, files in os.walk(directory):
                for filename in files:
                    filepath = os.path.join(root, filename)
                    file_paths.append(filepath)  # Add it to the list.
            return file_paths

        files_path = get_filepaths(inputDir)
        if not os.path.exists(outputDir):
            os.mkdir(outputDir)
        print("Start...\n")
        self.file_frequency(files_path, outputDir)
        self.common_frequency(files_path, outputDir)
        print("Finished!\n")


wp = WordProcessor()
inputDir = "D:\\download\\test"  # 所有待统计的文章都放在此目录下
outputDir = "D:\\download\\output"  # 此目录存放所有输出结果（包含各文章词频，和共词频），注：不能跟inputDir同目录
wp.calculate_frequency(inputDir, outputDir)
