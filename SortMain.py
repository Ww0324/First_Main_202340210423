# 团队排序算法整合项目 - 初始框架
# 项目名称：First_Main_202340210423
# 开发规范：遵循驼峰命名、注释完整、格式统一
# 排序算法函数预留区域：组内成员依次在下方添加自己的算法
# 示例格式：def zsBubbleSort(arr)

# 选择排序
# 功能：对数字数组进行升序排序
# 参数：arr - 待排序的数字数组
# 返回值：sortedArr - 排序后的升序数组
def ljySelectSort(arr):
    # 复制原数组，避免修改原数组
    sortedArr = arr.copy()
    n = len(sortedArr)

    # 外层循环：依次确定每一轮最小值的位置
    for i in range(n - 1):
        minIndex = i

        # 内层循环：找到当前未排序部分的最小值下标
        for j in range(i + 1, n):
            if sortedArr[j] < sortedArr[minIndex]:
                minIndex = j

        # 交换当前位置元素和最小值元素
        if minIndex != i:
            sortedArr[i], sortedArr[minIndex] = sortedArr[minIndex], sortedArr[i]

    return sortedArr

if __name__ == '__main__':
    # 测试数组：统一使用该数组验证排序效果，保证一致性
    testArr = [9, 3, 7, 1, 5, 8, 2, 6, 4]

    print("原始测试数组：", testArr)

    # 成员调用自己的算法：后续在此处添加代码