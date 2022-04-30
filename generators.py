import random

class PRNG(object):

    """
        Pseudorandom Number Generator.
        Class responsible for containing attributes and methods common to PRNGs
        self.seed = seed to be used in the generator, must have
                truly random origin
        self.length = length of number to generate
    """
    def __init__(self, seed, length):
        self.seed = seed
        self.length = length


    """
     Returns a list of prime numbers up to the value 'max'
        using the sieve method of Eratosthenes  
    """
    def get_list_of_primes(self, max):
        primes = list()
        not_primes = list()
        for i in range(2, max + 1):
            if i not in not_primes:
                primes.append(i)
                for j in range(i * i, max + 1, i):
                    not_primes.append(j)
        return primes


    """
       Checks if values ​​v1 and v2 are coprime to each other
    """
    def are_coprimes(self, v1, v2):
        while v2 != 0:
            v1, v2 = v2, (v1 % v2)
        return v1 == 1

class BBS(PRNG):
    """
       Blum Blum Shub Algorithm.
        Inherits parent PRNG class.
    """
    def __init__(self, seed, length):
        super(BBS, self).__init__(seed, length)

    """
      Method used to generate n, which is the product
        multiplication of the prime numbers p and q.
        Checks modulo 4 == 3, value greater than one
        threshold (used to generate large numbers), in addition to
        to check whether p and q are coprimes of each other.
    """
    def get_n(self):
        # valor minimo para o valor de p e q
        threshold = 7000
        # retorna uma lista de números primos até 100000
        primes = self.get_list_of_primes(10000)
        while True:
            p = random.choice(primes)
            # faz verificações do número escolhido
            if (((p % 4) == 3) and p > threshold):
                break
        while True:
            q = random.choice(primes)
            # faz verificações do número escolhido
            if (((q % 4) == 3) and q > threshold):
                # faz a verificação de co-primos
                if ((p != q) and self.are_coprimes(self.seed, p*q)):
                    break
        return p * q


    """
       Method used to effectively generate the number
        pseudorandom.
        is_default indicates whether to use the values
        previously set p and q, where p = 70891 and q = 85247.
        If the value is false, use the get_n() function to
        generate the values ​​of p and q, increasing the complexity of the
        algorithm.
        Effective each step of the algorithm execution
    """
    def generate_number(self, is_default=True):
        if is_default:
            p = 70891
            q = 85247
            n = p * q
        else:
            n = self.get_n()
        x = list()
        b = list()
        x.append((self.seed ** 2) % n) # atribuição de x[0]
        for i in range(self.length):
            # atribuição de Xi de acordo com algoritmo
            x.append((x[-1]**2) % n)
            # atribuição de Bi de acordo com algoritmo
            b.append(x[-1] % 2)
        # Agrupa valores de Bi como uma string para
        # setar self.generated_number, variável onde
        # estará armazenado o número pseudoaleatório
        # final gerado.
        self.generated_number = ''.join(map(str, b))
        return True


class LCG(PRNG):
    """
        Linear Congruential Generator Algorithm.
        Inherits parent PRNG class.
        Makes all checks according to the rules
        of the algorithm for the variables m, a, c and x0.
        length and x0 will be assigned to inherited attributes
        of the PRNG class self.length and self.seed.
    """
    def __init__(self, length, m, a, c, x0):
        if m <= 0:
            raise ValueError('m must be > 0')
        if a <= 0:
            raise ValueError('a must be > 0')
        if a >= m:
            raise ValueError('a must be < m')
        if c < 0:
            raise ValueError('c must be >= 0')
        if c >= m:
            raise ValueError('c must be < m')
        if x0 < 0:
            raise ValueError('x0 must be >= 0')
        if c >= m:
            raise ValueError('x0 must be < m')
        self.m = m
        self.a = a
        self.c = c
        super(LCG, self).__init__(x0, length)


    """
        Effectively generates the pseudo-random number through
        of the equivalent algorithm and the configured attributes
        in the class constructor.
    """
    def generate_number(self):
        x = list()
        # Adiciona a semente 'seed' ao valor inicial de X
        x.append(self.seed)
        # De acordo com o tamanho desejado, gera os valores
        # que devem ser concatenados
        for i in range(self.length):
            # Adiciona em X o calculo ((a*X(n-1) + c) mod m))
            # de acordo com regras do algoritmo
            x.append((self.a * x[-1] + self.c) % self.m)
        # armazena o número pseudo-aleatório gerado na variável
        # self.generated_number
        self.generated_number = ''.join(map(str,x))



class MT(PRNG):
    """
        Mersenne Twister algorithm.
    """
    def __init__(self, seed):
        super(MT, self).__init__(seed)
