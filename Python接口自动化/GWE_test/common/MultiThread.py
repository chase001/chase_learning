import threadpool, os
from common.func import *
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed


def cost_time_cal(func):
    """消耗时间计算装饰器"""

    def warp(*args):
        start_time = time.time()
        func(*args)
        print("******  Concurrrent test is end, Total cost {}S  ******".format(round(time.time() - start_time, 2)))

    return warp


def cal_weight(name, weight, unit="斤"):
    # num, name, a = args
    # print("Hello,{name} is {num} {unit}".format(name=name, num=weight, unit=unit))
    time.sleep(1)
    return "Hello,{name}{num}{unit}".format(name=name, num=weight, unit=unit)


def cal_weight_2(name_weight_list, unit="斤"):
    # num, name, a = args
    # for l in name_weight_list:
    # print("Hello,{name} is {num} {unit}".format(name=l[0], num=l[1], unit=unit))
    time.sleep(1)
    return "Hello,{name}{num}{unit}".format(name=name_weight_list[0], num=name_weight_list[1], unit=unit)


class ConcurrentTools(object):
    """
    目前使用两种并发库，threadpool和concurrent
    从并发速度考虑，优先建议使用 run_concurrrent_threadpool
    """

    def __init__(self, process_worker_quantity=None, thread_worker_quantity=None):
        self.process_worker_quantity = process_worker_quantity if process_worker_quantity else os.cpu_count()
        self.thread_worker_quantity = thread_worker_quantity if thread_worker_quantity else os.cpu_count() * 5

    # @cost_time_cal
    def run_thread_pool(self, threads_num, request_num, target_request):
        """
        用于创建线程池
        :param threads_num: 线程数量
        :param request_num: 参数列表
        :param target_request: 需要运行的函数
        :return:
        """
        # log.info(msg="Ready for {func_name} MultiThread running!!".format(func_name=target_request.__name__))
        log.info(msg="Starting at {now}".format(now=now()))
        pool = threadpool.ThreadPool(num_workers=threads_num)
        requests = threadpool.makeRequests(target_request, request_num)
        [pool.putRequest(req) for req in requests]
        pool.wait()
        log.info(msg="End at {now}".format(now=now()))

    # @cost_time_cal
    def run_concurrrent_threadpool(self, func, ls, *args):
        """
        Concurrent 线程池方法
        :param thread_num: 线程数量，默认为cpu数量*2
        :param func: 被执行函数
        :param args: 可变参数
        :return:返回被执行函数的结果集
        """
        result_list = []
        with ThreadPoolExecutor(thread_name_prefix="my_thread") as executor:
            future_tasks = [executor.submit(func, l, *args) for l in ls]

            for future in as_completed(future_tasks):
                result_list.append(future.result())  # 循环取出运行结果

            return result_list

    # 不建议使用
    @cost_time_cal
    def run_concurrrent_processpool(self, func, *args):
        """
        这个模块实现的是真正的并行计算，因为它使用ProcessPoolExecutor类把工作分配给多个Python进程处理。因此，如果需要做CPU 密集型处理，
        使用这个模块能绕开GIL，利用所有可用的CPU核心。
        :param thread_num: 进程数量
        :param func: 被执行函数
        :param args: 可变参数
        :return:
        """
        # with ProcessPoolExecutor() as executor:
        #     future_tasks = [executor.submit(func, l, *args) for l in ls]
        #     for f in future_tasks:
        #         print(f.result()) if f.result() else None
        result_list = []
        with ProcessPoolExecutor() as executor:
            for number in executor.map(func, *args):
                print("{}".format(1))
                # for number, prime in zip(ls, executor.map(func, ls),):
                #     print('%d is prime: %s' % (number, prime))

                # for future in as_completed(future_tasks):
                #     result_list.append(future.result())  # 循环取出运行结果
                #
                # return result_list

    @cost_time_cal
    def run_concurrrent_process_thread_pool(self, func, arg_list, time_out=None):
        """
        用于多进程和多线程并发侧测试
        Args:
            fn : 被测方法
            arg_list : 被测方法中使用的可迭代的参数列表
            time_out : 线程等待的最大秒数。如果不传，那么等待时间就没有限制
        """
        log.info("\n****** Concurrrent Test Start ******"
                 "\n***** Target Function is {} ******"
                 "\n***** Process Quanlity is {} ******"
                 "\n***** Thread Quanlity is {} ******".format(func.__name__, self.process_worker_quantity,
                                                               self.thread_worker_quantity))
        result_list = []
        div_arg_list = self._div_list(arg_list, self.thread_worker_quantity)
        print(div_arg_list)
        with ProcessPoolExecutor(max_workers=self.process_worker_quantity) as e:
            process_futures = [e.submit(self._thread_worker, func, i, time_out) for i in div_arg_list]
            for process_future in process_futures:
                for thread_result in process_future.result():
                    log.info(thread_result)
                    result_list.append(thread_result)
            log.info("Concurrrent Test is END")
            return result_list

    def _thread_worker(self, func, sub_arg_list, time_out):
        future_result_list = []
        with ThreadPoolExecutor(max_workers=self.thread_worker_quantity) as e:
            futures = [e.submit(func, i) for i in sub_arg_list]
            # for i in sub_arg_list:
            #     futures_dict = {str(i): future for future in [e.submit(func, i)]}
            #     futures_list.append(futures_dict)

            for future in as_completed(futures, timeout=time_out):
                if future.exception() is not None:
                    log.warning("线程报错,{msg}".format(msg=future.exception()))
                else:
                    future_result_list.append(future.result())
            return future_result_list

    def _div_list(self, init_list, childern_list_len):
        # result = []
        # cut = int(len(ls) / n)
        # if cut == 0:
        #     ls = [[x] for x in ls]
        #     none_array = [[] for i in range(0, n - len(ls))]
        #     return ls + none_array
        # for i in range(0, n - 1):
        #     result.append(ls[cut * i:cut * (1 + i)])
        # result.append(ls[cut * (n - 1):len(ls)])
        # return result
        list_of_groups = zip(*(iter(init_list),) * childern_list_len)
        end_list = [list(i) for i in list_of_groups]
        count = len(init_list) % childern_list_len
        end_list.append(init_list[-count:]) if count != 0 else end_list
        return end_list


# class Particle:
#     def __init__(self, i):
#         self.i = i
#         self.fitness = None
#
#     def getfitness(self):
#         self.fitness = 2 * self.i
#
#
# def thread_worker(p):
#     p.getfitness()
#     return (p.i, p)

def proc_worker(ps):
    import concurrent.futures as cf
    s = time.time()
    with cf.ThreadPoolExecutor() as e:
        result = list(e.map(cal_weight_2, ps))

    print("Thread COST:{}".format(time.time() - s))
    return result


# @cost_time_cal
def update_fitness(INFO):
    import concurrent.futures as cf
    with cf.ProcessPoolExecutor() as e:
        for result_list in e.map(proc_worker, INFO):
            for l in result_list:
                print(l)
                # print (result_list)


def div_list(ls, n):
    result = []
    cut = int(len(ls) / n)
    if cut == 0:
        ls = [[x] for x in ls]
        none_array = [[] for i in range(0, n - len(ls))]
        return ls + none_array
    for i in range(0, n - 1):
        result.append(ls[cut * i:cut * (1 + i)])
    result.append(ls[cut * (n - 1):len(ls)])
    return result
    # result=[]
    # for i in range(0,len(ls),n):
    #     result.append(ls[i:i+n])
    # return result


if __name__ == '__main__':
    # MultiThread.run_thread_pool(4,['xiaozi','aa','bb','cc'],sayhello)
    names = ["yuting", "shuhuai", "cuirong", "panda", "xxx"]
    weight = [150, 150, 150, 150, 150]
    # # #a = "斤"
    # MultiThread.run_concurrrent_threadpool(cal_weight, names,weight)
    # #
    # concurrenttools.run_concurrrent_processpool(cal_weight,names,weight )

    # particles = [Particle(i) for i in range(500)]
    # check all(particles[i].i == i for i in range(len(particles)))

    # check all(particles[i].i == i for i in range(len(particles)))
    # check all(p.fitness == 2 * p.i for p in particles)
    # l = div_list(list(zip(names, weight)) * 16, 4)
    l = list(zip(names, weight)) * 16
    # print(l)
    concurrenttools = ConcurrentTools(thread_worker_quantity=13)
    concurrenttools.run_concurrrent_process_thread_pool(cal_weight_2, l)
