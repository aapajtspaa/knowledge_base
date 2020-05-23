import jieba
import os
import pickle
from numpy import *
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets.base import Bunch
from sklearn.naive_bayes import MultinomialNB
import time


def fengzhuang(x):
    file = open('test1/待分类文本/1.txt', 'w+', encoding='UTF-8')
    a = x
    print(a, file=file)
    file.close()

    file = open('test1/待分类文本/1.txt', 'r', encoding='UTF-8')
    sent = file.read()
    sent_list = jieba.cut(sent)
    #
    file0 = open('split/test_split/待分类文本/1.txt', 'w+', encoding='UTF-8')
    file0.write(' '.join(sent_list))
    file.close()
    file0.close()
    start = time.time()

    def readFile(path):
        with open(path, 'r', errors='ignore') as file:  # 文档中编码有些问题，所有用errors过滤错误
            content = file.read()
            file.close()
            return content

    def saveFile(path, result):
        with open(path, 'w', errors='ignore') as file:
            file.write(result)
            file.close()

    def segText(inputPath, resultPath):
        fatherLists = os.listdir(inputPath)  # 主目录
        for eachDir in fatherLists:  # 遍历主目录中各个文件夹
            eachPath = inputPath + eachDir + "/"  # 保存主目录中每个文件夹目录，便于遍历二级文件
            each_resultPath = resultPath + eachDir + "/"  # 分词结果文件存入的目录
            if not os.path.exists(each_resultPath):
                os.makedirs(each_resultPath)
            childLists = os.listdir(eachPath)  # 获取每个文件夹中的各个文件
            for eachFile in childLists:  # 遍历每个文件夹中的子文件
                eachPathFile = eachPath + eachFile  # 获得每个文件路径
                content = readFile(eachPathFile)  # 调用上面函数读取内容
                result = (str(content)).replace("\r\n", "").strip()  # 删除多余空行与空格

                cutResult = jieba.cut(result)  # 默认方式分词，分词结果用空格隔开
                saveFile(each_resultPath + eachFile, " ".join(cutResult))  # 调用上面函数保存文件

    def bunchSave(inputFile, outputFile):
        catelist = os.listdir(inputFile)
        bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
        bunch.target_name.extend(catelist)  # 将类别保存到Bunch对象中
        for eachDir in catelist:
            eachPath = inputFile + eachDir + "/"
            fileList = os.listdir(eachPath)
            for eachFile in fileList:  # 二级目录中的每个子文件
                fullName = eachPath + eachFile  # 二级目录子文件全路径
                bunch.label.append(eachDir)  # 当前分类标签
                bunch.filenames.append(fullName)  # 保存当前文件的路径
                bunch.contents.append(readFile(fullName).strip())  # 保存文件词向量
        with open(outputFile, 'wb') as file_obj:  # 持久化必须用二进制访问模式打开
            pickle.dump(bunch, file_obj)

    def readBunch(path):
        with open(path, 'rb') as file:
            bunch = pickle.load(file)
        return bunch

    def writeBunch(path, bunchFile):
        with open(path, 'wb') as file:
            pickle.dump(bunchFile, file)

    def getStopWord(inputFile):
        stopWordList = readFile(inputFile).splitlines()
        return stopWordList

    def getTestSpace(testSetPath, trainSpacePath, stopWordList, testSpacePath,
                     testSpace_path, testSpace_arr_path, trainbunch_vocabulary_path):
        bunch = readBunch(testSetPath)
        testSpace = Bunch(target_name=bunch.target_name, label=bunch.label, filenames=bunch.filenames, tdm=[],
                          vocabulary={})
        testSpace_out = str(testSpace)
        saveFile(testSpace_path, testSpace_out)
        trainbunch = readBunch(trainSpacePath)
        vectorizer = TfidfVectorizer(stop_words=stopWordList, sublinear_tf=True, max_df=0.5,
                                     vocabulary=trainbunch.vocabulary)
        transformer = TfidfTransformer()
        testSpace.tdm = vectorizer.fit_transform(bunch.contents)
        testSpace.vocabulary = trainbunch.vocabulary
        testSpace_arr = str(testSpace.tdm)
        trainbunch_vocabulary = str(trainbunch.vocabulary)
        saveFile(testSpace_arr_path, testSpace_arr)
        saveFile(trainbunch_vocabulary_path, trainbunch_vocabulary)
        writeBunch(testSpacePath, testSpace)

    def bayesAlgorithm(trainPath, testPath, tfidfspace_out_arr_path,
                       tfidfspace_out_word_path, testspace_out_arr_path,
                       testspace_out_word_apth):
        trainSet = readBunch(trainPath)
        testSet = readBunch(testPath)
        clf = MultinomialNB(alpha=0.001).fit(trainSet.tdm, trainSet.label)
        tfidfspace_out_arr = str(trainSet.tdm)  # 处理
        tfidfspace_out_word = str(trainSet)
        saveFile(tfidfspace_out_arr_path, tfidfspace_out_arr)  # 矩阵形式的train_set.txt
        saveFile(tfidfspace_out_word_path, tfidfspace_out_word)  # 文本形式的train_set.txt

        testspace_out_arr = str(testSet)
        testspace_out_word = str(testSet.label)
        saveFile(testspace_out_arr_path, testspace_out_arr)
        saveFile(testspace_out_word_apth, testspace_out_word)
        predicted = clf.predict(testSet.tdm)
        for flabel, fileName, expect_cate in zip(testSet.label, testSet.filenames, predicted):
            print(fileName, flabel, "-->预测类别：", expect_cate)
        return expect_cate

    segText(datapath,  # 读入数据
            split_datapath)  # 输出分词结果
    bunchSave(split_datapath,  # 读入分词结果
              train_dat_path)  # 输出分词向量
    stopWordList = getStopWord(stopWord_path)  # 获取停用词表
    # 输入测试集
    segText(test_path,
            test_split_path)  # 对测试集读入文件，输出分词结果
    bunchSave(test_split_path,
              test_split_dat_path)  #
    getTestSpace(test_split_dat_path,
                 tfidfspace_dat_path,
                 stopWordList,
                 testspace_dat_path,
                 testSpace_path,
                 testSpace_arr_path,
                 trainbunch_vocabulary_path)  # 输入分词文件，停用词，词向量，输出特征空间(txt,dat文件都有)
    resultReturn = bayesAlgorithm(tfidfspace_dat_path,
                                  testspace_dat_path,
                                  tfidfspace_out_arr_path,
                                  tfidfspace_out_word_path,
                                  testspace_out_arr_path,
                                  testspace_out_word_apth)
    print(resultReturn)
    end = time.time()
    print(end - start)


datapath = "./data/"  # 原始数据路径
stopWord_path = "stop/stopword.txt"  # 停用词路径
test_path = "test1/"  # 测试集路径
test_split_dat_path = "test_set.dat"  # 测试集分词bat文件路径
testspace_dat_path = "testspace.dat"  # 测试集输出空间矩阵dat文件
train_dat_path = "train_set.dat"  # 读取分词数据之后的词向量并保存为二进制文件
tfidfspace_dat_path = "tfidfspace.dat"  # tf-idf词频空间向量的dat文件
test_split_path = 'split/test_split/'  # 测试集分词路径
split_datapath = "./split/split_data/"  # 对原始数据分词之后的数据路径
testSpace_path = "testSpace.txt"  # 测试集分词信息
testSpace_arr_path = "testSpace_arr.txt"  # 测试集词频矩阵信息
trainbunch_vocabulary_path = "trainbunch_vocabulary.txt"  # 所有分词词频信息
tfidfspace_out_arr_path = "tfidfspace_out_arr.txt"  # tfidf输出矩阵信息
tfidfspace_out_word_path = "tfidfspace_out_word.txt"  # 单词形式的txt
testspace_out_arr_path = "testspace_out_arr.txt"  # 测试集输出矩阵信息
testspace_out_word_apth = "./testspace_out_word.txt"  # 测试界单词信息
# 输入训练集


fengzhuang(input('病症：'))
