# 团队排序算法整合项目 - 初始框架
# 项目名称：First_Main_202340210423
# 开发规范：遵循驼峰命名、注释完整、格式统一

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

# ========== 排序算法函数预留区域 ==========
# 组内成员依次在下方添加自己的算法
# 示例格式：def 姓名首拼_算法名(参数): 如 zsBubbleSort(arr)

# 曾莹 - 快速排序算法
# 快速排序
# 功能：对数字数组进行升序排序
# 参数：arr - 待排序的数字数组
# 返回值：sortedArr - 排序后的升序数组
def zyQuickSort(arr):
    """
    快速排序算法实现
    采用分治策略：选择一个基准元素，将数组分成左右两部分，
    左边部分所有元素小于等于基准，右边部分所有元素大于基准，
    然后递归地对左右两部分进行排序

    参数：
        arr: list - 待排序的数组
    返回：
        list - 排序后的升序数组
    """
    # 复制原数组，避免修改原数据
    sortedArr = arr.copy()

    # 定义内部递归排序函数
    def _quick_sort(items, low, high):
        """
        递归执行快速排序

        参数：
            items: list - 待排序的子数组
            low: int - 子数组的起始索引
            high: int - 子数组的结束索引
        """
        if low < high:
            # 分区操作，获取基准元素的最终位置
            pi = _partition(items, low, high)
            # 递归排序基准左侧的子数组
            _quick_sort(items, low, pi - 1)
            # 递归排序基准右侧的子数组
            _quick_sort(items, pi + 1, high)

    def _partition(items, low, high):
        """
        分区函数：将数组划分为两部分

        参数：
            items: list - 待分区的子数组
            low: int - 起始索引
            high: int - 结束索引
        返回：
            int - 基准元素的最终位置索引
        """
        # 选择最右边的元素作为基准值
        pivot = items[high]
        # i指向小于基准区域的最后一个元素
        i = low - 1

        # 遍历数组，将小于等于基准的元素放到左侧
        for j in range(low, high):
            if items[j] <= pivot:
                i = i + 1
                # 交换元素
                items[i], items[j] = items[j], items[i]

        # 将基准元素放到正确的位置
        items[i + 1], items[high] = items[high], items[i + 1]
        # 返回基准元素的位置
        return i + 1

    # 调用递归排序函数，对整个数组进行排序
    _quick_sort(sortedArr, 0, len(sortedArr) - 1)
    return sortedArr


# ========== 其他组员算法将添加在此处 ==========
# （组内其他成员在此添加各自的排序算法）


# ========== 程序运行测试入口 ==========
if __name__ == '__main__':
    # 测试数组：统一使用该数组验证排序效果，保证一致性
    testArr = [9, 3, 7, 1, 5, 8, 2, 6, 4]

    # 调用自己的排序算法
    print("原始测试数组：", testArr)