# Import flask and datetime module for showing date and time
from flask import Flask, request
  
# Initializing flask app
app = Flask(__name__)

import os
os.environ["SETUPTOOLS_USE_DISTUTILS"] = "stdlib"
index = [1907, 1237, 659, 499, 188, 3440, 3564, 4312, 3871, 3521, 1407, 2583, 1909, 3954, 1507, 308, 3792, 368, 3811, 15, 1971, 198, 2669, 1066, 1557, 2318, 858, 1241, 699, 2754, 428, 2221, 1132, 2998, 2436, 2967, 564, 1265, 46, 1130, 3916, 2379, 782, 2918, 1639, 3698, 3367, 1140, 804, 3832, 2443, 1882, 616, 3004, 817, 4215, 663, 3959, 4223, 1520, 3493, 2296, 1973, 1884, 491, 1050, 1168, 2984, 824, 2827, 416, 1010, 2747, 229, 1938, 2089, 4209, 3481, 898, 2087, 3086, 1736, 2024, 4069, 1152, 3093, 3365, 2168, 2084, 1446, 3582, 3171, 2743, 3446, 3268, 4061, 1765, 3179, 1172, 273, 2831, 2414, 4287, 3928, 397, 395, 2102, 3, 1638, 734, 3671, 4063, 251, 4139, 2464, 2820, 569, 1886, 3253, 201, 3625, 514, 2061, 1950, 3439, 3710, 2399, 484, 1449, 1511, 380, 3213, 1818, 2680, 4406, 500, 3526, 3411, 2652, 95, 2416, 941, 1475, 1351, 1878, 4143, 551, 656, 2439, 4233, 1144, 4094, 1453, 1970, 2616, 1864, 1694, 1559, 371, 1814, 646, 2105, 1236, 2657, 3172, 1074, 2937, 3809, 541, 1960, 555, 2451, 4165, 355, 1547, 2185, 2660, 4407, 2188, 2394, 4117, 3359, 1386, 3787, 2474, 2946, 1513, 1400, 3514, 2596, 324, 1178, 3760, 1110, 4387, 1216, 570, 2679, 4205, 1719, 653, 4082, 4360, 2032, 263, 1031, 3512, 2893, 3739, 1898, 1209, 2897, 2778, 2133, 3836, 342, 1465, 774, 2761, 1846, 2936, 1049, 2263, 1435, 2765, 2100, 1538, 4179, 788, 1028, 2593, 22, 3221, 3630, 2733, 4248, 1244, 4198, 2494, 4126, 999, 1976, 411, 2083, 544, 3511, 503, 862, 4317, 4103, 2052, 3558, 4152, 2205, 2234, 3943, 2795, 1024, 1839, 237, 4023, 2840, 741, 877, 1579, 2649, 4160, 3344, 866, 3335, 2868, 1717, 1661, 1014, 482, 442, 705, 422, 621, 806, 1728, 438, 3571, 162, 763, 86, 3659, 704, 3765, 2903, 3129, 2112, 3673, 700, 4375, 104, 4187, 631, 786, 466, 3039, 4423, 1436, 793, 1595, 4468, 3212, 2884, 2670, 276, 2264, 2256, 4338, 2719, 759, 2036, 2894, 3919, 3961, 813, 1808, 4127, 2698, 1596, 4403, 3083, 1599, 3053, 3885, 1012, 3737, 1380, 4224, 1129, 1590, 3586, 912, 2214, 2714, 4433, 3864, 173, 316, 2417, 134, 3922, 3915, 1681, 3296, 1433, 3189, 2716, 1126, 1206, 3248, 3793, 761, 4405, 2812, 2859, 3187, 2015, 4495, 1083, 4176, 4092, 3480, 4119, 1523, 2413, 191, 3939, 4348, 189, 4084, 3876, 3679, 2910, 2702, 2822, 98, 2481, 747, 1637, 3220, 2472, 3841, 216, 1307, 2246, 943, 973, 4453, 3852, 3668, 3837, 3888, 1275, 4361, 2516, 2988, 1584, 3713, 2619, 1631, 2361, 2711, 1412, 625, 1778, 1757, 4042, 1149, 3202, 3580, 2237, 2797, 3670, 2589, 1175, 2927, 1006, 3597, 385, 871, 468, 546, 3222, 1100, 2803, 4446, 3251, 140, 2224, 1903, 3533, 1567, 3002, 2870, 3461, 1987, 1264, 701, 2544, 3500, 844, 1310, 3761, 1272, 896, 3797, 4470, 581, 2160, 444, 3413, 1457, 1563, 3099, 351, 1073, 1651, 1821, 2883, 854, 535, 301, 4494, 744, 1800, 678, 443, 1484, 3989, 138, 3614, 3933, 3843, 2555, 4100, 236, 4247, 1496, 2567, 3575, 4085, 1077, 1278, 2496, 149, 1785, 2314, 525, 298, 1871, 1928, 2801, 952, 262, 1331, 3389, 3060, 3261, 724, 3014, 2549, 3121, 3925, 3183, 1921, 1052, 3360, 3432, 928, 1139, 4334, 2788, 3078, 2811, 3701, 1023, 2137, 64, 1952, 1606, 1858, 1585, 962, 28, 600, 1474, 2916, 815, 3994, 3437, 1108, 3579, 4302, 1863, 1658, 3076, 2541, 2060, 1777, 2116, 2392, 4311, 4454, 2634, 3371, 3950, 3504, 224, 3838, 3321, 40, 2570, 2405, 2689, 1969, 2068, 1829, 1019, 3559, 1416, 729, 4430, 2367, 4230, 3973, 2663, 129, 684, 2768, 2794, 892, 3724, 1745, 2790, 1543, 2123, 2165, 574, 1654, 2594, 2511, 2290, 1239, 554, 3561, 599, 1792, 1875, 1141, 719, 3640, 924, 3877, 2184, 1068, 4053, 1522, 413, 4261, 177, 4353, 1628, 326, 961, 3350, 2144, 3824, 3308, 1571, 2784, 2408, 2952, 2370, 3038, 1688, 617, 639, 4358, 3862, 3226, 4480, 490, 1402, 3822, 2625, 1417, 2838, 3957, 694, 2632, 972, 891, 2767, 4351, 2863, 3348, 321, 4274, 1754, 640, 2534, 732, 933, 2364, 206, 3505, 2169, 1962, 2523, 507, 1311, 2182, 2373, 627, 865, 1773, 1039, 822, 1062, 2744, 4350, 4422, 426, 1058, 3996, 1726, 3524, 123, 2824, 1711, 1844, 103, 2158, 4321, 1991, 2044, 3725, 9, 2665, 69, 2908, 3077, 4002, 447, 4390, 2173, 3416, 2001, 716, 1920, 1434, 1080, 1349, 948, 347, 1438, 1600, 4016, 496, 560, 4486, 1069, 3867, 3217, 384, 3231, 4080, 2233, 1179, 1656, 2329, 1890, 847, 2395, 1985, 2878, 714, 3003, 2817, 4414, 1322, 4142, 3144, 955, 1852, 2423, 2272, 296, 2947, 3938, 3632, 4210, 4175, 1997, 3721, 3755, 2752, 925, 2347, 1315, 676, 2641, 2486, 2547, 1755, 1242, 1822, 4272, 1029, 2491, 850, 3051, 820, 4190, 843, 2050, 2930, 2368, 2603, 181, 4141, 2191, 2375, 3247, 37, 3250, 277, 2172, 2703, 1432, 2701, 2420, 3306, 4289, 208, 597, 1838, 1966, 2157, 1500, 2809, 337, 1957, 4183, 3337, 2857, 3370, 2268, 534, 1222, 1065, 4440, 287, 1721, 4392, 3813, 2762, 1093, 712, 101, 722, 260, 1064, 4278, 2537, 3366, 4189, 1274, 4426, 3105, 3641, 148, 4307, 1285, 1495, 1273, 4496, 3185, 2432, 706, 702, 1240, 2872, 2881, 1865, 2668, 1510, 1254, 3267, 2051, 614, 3962, 4173, 2560, 4125, 2252, 4138, 2352, 3293, 4089, 6, 1341, 3326, 2579, 552, 1054, 4134, 3055, 1537, 4114, 1964, 4239, 1447, 703, 1561, 2724, 1913, 450, 1425, 696, 4356, 3154, 1454, 1227, 3408, 43, 204, 1137, 4452, 2166, 3744, 2958, 2140, 830, 3444, 3108, 4368, 3946, 3400, 1701, 3677, 2706, 3993, 360, 932, 1935, 1901, 333, 612, 1445, 1805, 2365, 2604, 2728, 2917, 2531, 4159, 339, 2685, 1188, 3433, 487, 2197, 2304, 1670, 2270, 511, 2258, 1266, 417, 2882, 271, 1615, 709, 1448, 882, 2181, 776, 1223, 1652, 1259, 2283, 1666, 3087, 3079, 414, 1159, 2888, 2415, 4050, 3631, 2322, 2590, 3209, 3412, 458, 3903, 1653, 90, 3736, 3890, 717, 720, 2163, 767, 2007, 3463, 2584, 1472, 1021, 3574, 1793, 2600, 225, 4051, 2580, 1643, 2964, 853, 1363, 4444, 2046, 1854, 3043, 809, 439, 1498, 3387, 4398, 2120, 2077, 286, 3964, 993, 2081, 4229, 1551, 3688, 2094, 1761, 242, 3462, 3096, 867, 3952, 2404, 1676, 2056, 3334, 3047, 5, 1963, 851, 1847, 3239, 4432, 4345, 3285, 2780, 2513, 375, 3029, 1626, 787, 3603, 4438, 799, 587, 3722, 2843, 1355, 1990, 1933, 842, 3768, 3921, 4485, 860, 2944, 3540, 2183, 3758, 2440, 2737, 589, 243, 1393, 455, 91, 2736, 3020, 3085, 3802, 2965, 127, 222, 3735, 2651, 4448, 2880, 4291, 3911, 3122, 4098, 4200, 3186, 209, 2053, 1174, 4129, 1834, 427, 288, 1312, 3233, 801, 2591, 753, 4204, 1550, 1981, 3182, 1001, 611, 1993, 2695, 3563, 4057, 1267, 3385, 4354, 1702, 3920, 2009, 2048, 2397, 493, 2257, 1381, 2749, 1672, 4150, 2650, 1269, 2810, 2645, 2850, 1243, 2853, 897, 3393, 3979, 964, 1280, 3205, 4079, 4071, 2300, 4043, 3021, 1165, 4161, 3031, 687, 2324, 4455, 2078, 184, 3894, 25, 1876, 2748, 4076, 2508, 3990, 3550, 4088, 2892, 3819, 1281, 1791, 4136, 2251, 982, 2218, 2507, 3534, 3454, 2618, 553, 4202, 1807, 2374, 636, 2049, 4332, 3383, 485, 3717, 4026, 4270, 1738, 2925, 3731, 4498, 4352, 1357, 1826, 1911, 1803, 3917, 1205, 3349, 970, 3396, 532, 2485, 3279, 2951, 4460, 3814, 1015, 1327, 598, 282, 1034, 1752, 4007, 174, 4116, 2602, 1346, 3275, 436, 4111, 771, 3775, 2463, 2316, 3602, 4477, 2194, 1382, 3992, 3200, 386, 940, 1231, 1763, 210, 2497, 2479, 266, 4330, 2781, 527, 3472, 2686, 2455, 312, 3485, 167, 803, 4181, 33, 1486, 4262, 1203, 1262, 3441, 3501, 1686, 117, 1221, 1234, 666, 3848, 135, 4282, 2294, 4168, 2520, 2148, 4004, 4194, 1071, 3375, 1217, 2382, 2842, 3091, 730, 2666, 1026, 1195, 2750, 698, 987, 3116, 3133, 75, 1467, 3290, 2498, 144, 3694, 245, 1646, 41, 4457, 4174, 3450, 2450, 1347, 4298, 3118, 3866, 168, 3065, 980, 111, 1809, 695, 3612, 1764, 3899, 3643, 610, 1183, 3134, 1603, 4265, 2837, 986, 3381, 3242, 1301, 2924, 1645, 647, 833, 1788, 1154, 1836, 2462, 2226, 54, 267, 2690, 2428, 4212, 1442, 47, 4019, 2911, 3395, 680, 486, 3623, 879, 797, 233, 3229, 2821, 2477, 2042, 4285, 679, 2308, 448, 4347, 3196, 3742, 4439, 545, 2267, 2338, 1095, 1908, 2164, 3927, 2533, 3854, 1647, 2400, 440, 239, 3274, 630, 818, 1575, 2624, 2161, 196, 2606, 3052, 16, 3317, 2198, 2152, 279, 946, 1038, 3147, 4121, 3985, 2647, 3486, 2700, 3032, 2713, 2545, 1640, 304, 258, 3778, 1473, 2282, 1334, 3907, 1376, 4383, 3585, 3607, 2979, 323, 3875, 1423, 615, 3592, 1377, 3227, 4293, 566, 2109, 1536, 3567, 733, 1181, 3968, 1695, 2253, 1336, 1104, 3637, 112, 1833, 2994, 4015, 50, 4333, 218, 432, 3708, 784, 938, 1043, 2667, 1968, 1367, 1768, 1482, 1428, 309, 1359, 2391, 1419, 736, 4070, 1611, 576, 4031, 1238, 697, 3330, 2539, 1191, 3258, 1375, 3583, 2175, 2614, 3878, 1056, 3112, 1170, 3557, 522, 4499, 3448, 3329, 1880, 2468, 3058, 3095, 2446, 4157, 418, 4072, 1389, 1091, 3791, 2954, 1319, 2524, 3165, 3712, 590, 1497, 2637, 1461, 4409, 608, 353, 2978, 1813, 1675, 3833, 3465, 629, 3578, 4303, 2777, 3204, 359, 1158, 441, 3028, 400, 3562, 1782, 2063, 620, 3759, 685, 1710, 994, 4259, 205, 2608, 2244, 1005, 681, 4436, 2739, 3145, 3184, 3042, 4192, 1720, 1707, 1131, 2467, 182, 1304, 3249, 370, 228, 1491, 2096, 2250, 2962, 3552, 4177, 1749, 2209, 1429, 1801, 2135, 3315, 751, 810, 3407, 4429, 4324, 3683, 1851, 1657, 2800, 3853, 2495, 2740, 374, 227, 3415, 2095, 1354, 3553, 603, 2509, 1214, 1485, 1943, 2351, 3090, 585, 3080, 1007, 710, 2933, 1427, 1926, 80, 3794, 1582, 3642, 3618, 1042, 3714, 2890, 4196, 421, 424, 2613, 3645, 1399, 2939, 4257, 2745, 3981, 1698, 1094, 2983, 3767, 3466, 89, 969, 4329, 3844, 1516, 1161, 1426, 3976, 3945, 3168, 1360, 1576, 888, 223, 4388, 2045, 97, 2869, 3384, 1371, 1075, 1553, 725, 1554, 2764, 4437, 4296, 4421, 2755, 2325, 3605, 3856, 4145, 4101, 1345, 920, 800, 1739, 4211, 2022, 1283, 331, 3019, 2615, 3882, 2114, 4093, 1384, 1667, 4490, 3399, 2236, 3064, 1841, 66, 2384, 3693, 1036, 856, 1192, 4467, 2519, 3610, 2723, 3789, 4081, 4075, 3255, 1070, 1078, 1103, 1616, 2773, 3240, 2633, 1059, 3507, 4276, 71, 930, 2856, 1297, 2799, 641, 3223, 311, 2333, 3616, 671, 2577, 2174, 1975, 3977, 2190, 1799, 1772, 572, 1378, 547, 2475, 2358, 74, 133, 3288, 2091, 1439, 4466, 3868, 2528, 211, 3891, 3001, 1332, 3695, 389, 3970, 62, 1605, 2122, 4237, 2848, 2760, 1308, 2905, 2732, 3850, 2206, 2013, 3423, 1215, 4109, 3647, 758, 1560, 18, 2387, 4389, 537, 36, 1318, 3339, 2332, 2775, 1796, 3786, 634, 1641, 1201, 3074, 2240, 4316, 2738, 2067, 2476, 3681, 996, 2862, 4399, 816, 1546, 2348, 1819, 1870, 3682, 3596, 2653, 2383, 3482, 3664, 591, 1166, 723, 4068, 1514, 2086, 2107, 3805, 1794, 2847, 1348, 161, 998, 407, 2727, 2276, 376, 1565, 1271, 431, 366, 760, 481, 4280, 2033, 902, 1832, 1689, 1820, 2620, 3071, 1724, 17, 4219, 1431, 2145, 2323, 4018, 3880, 3243, 3897, 3398, 4191, 3947, 3570, 392, 583, 881, 4120, 1420, 4056, 3265, 826, 1996, 2480, 1700, 2412, 3098, 4047, 2741, 1385, 345, 471, 2628, 1394, 988, 1295, 58, 3358, 4420, 3723, 207, 1678, 3892, 770, 1564, 4124, 665, 2887, 2305, 3207, 3198, 4226, 3548, 1825, 2427, 690, 2804, 837, 2306, 1955, 3230, 3887, 1617, 1954, 4040, 985, 2825, 2192, 3611, 954, 1866, 2344, 1835, 904, 935, 1340, 126, 4028, 3026, 4357, 3115, 3208, 246, 2640, 991, 1233, 3499, 3103, 284, 280, 876, 984, 446, 601, 3646, 3457, 1942, 118, 2275, 2854, 1703, 1150, 3955, 3181, 2682, 2889, 4397, 454, 3665, 108, 1979, 156, 231, 1535, 2758, 381, 791, 2386, 1953, 3506, 682, 953, 1219, 2639, 3719, 558, 2418, 3699, 2672, 4314, 11, 4288, 1184, 4400, 916, 4104, 3464, 248, 4020, 3447, 2401, 4447, 3851, 2453, 878, 2378, 61, 12, 1257, 1362, 170, 637, 4279, 3700, 2901, 2623, 2559, 918, 332, 4461, 1904, 3910, 1815, 3652, 3254, 762, 1910, 1494, 78, 2622, 2970, 1998, 1837, 819, 1577, 981, 1849, 778, 735, 3264, 1369, 70, 315, 3644, 56, 1251, 3965, 1313, 4366, 4146, 796, 1662, 477, 178, 3931, 3487, 1155, 2816, 1481, 1194, 2961, 3518, 2504, 2675, 4054, 3859, 3782, 2518, 361, 939, 869, 769, 2403, 1335, 1760, 1200, 3402, 4231, 4427, 573, 501, 693, 1659, 1392, 2942, 3751, 4163, 1487, 1208, 2419, 3777, 4275, 1574, 4162, 3397, 562, 1632, 2708, 1977, 2457, 4066, 3756, 100, 1573, 1900, 1519, 4319, 7, 752, 926, 2430, 2311, 1333, 4077, 3113, 1488, 2090, 3422, 457, 3061, 3110, 2219, 2200, 750, 3347, 2235, 3166, 1758, 4067, 2210, 2431, 3696, 1298, 1562, 836, 1455, 2742, 2648, 4001, 2390, 4058, 840, 2923, 2020, 3940, 575, 4377, 240, 1459, 2503, 107, 3041, 2243, 2460, 2796, 832, 4258, 1978, 2855, 1840, 1441, 1352, 4349, 2576, 3354, 1937, 115, 1570, 2030, 2729, 3303, 2028, 2512, 974, 3178, 52, 2746, 3137, 1187, 3635, 1107, 3519, 261, 160, 4041, 2265, 707, 2759, 3298, 254, 3705, 1460, 2913, 3816, 3062, 2434, 3649, 1424, 4158, 3140, 4193, 299, 213, 4113, 2317, 977, 2465, 4365, 3109, 3377, 632, 3858, 919, 2232, 2195, 352, 4472, 708, 2106, 992, 4489, 2177, 4252, 3468, 3573, 4009, 3509, 1831, 2805, 320, 4166, 2054, 2844, 1951, 3235, 568, 379, 459, 171, 3434, 4151, 3730, 3974, 2016, 1683, 341, 960, 2808, 3067, 1946, 3982, 4242, 3322, 2343, 2852, 3271, 4133, 577, 2132, 451, 1894, 2231, 1587, 2005, 506, 2981, 580, 4180, 1041, 3547, 3452, 4404, 1816, 3173, 3978, 3314, 2581, 3528, 3278, 2059, 3252, 3795, 540, 3565, 4095, 194, 4264, 2955, 1167, 1199, 4065, 4449, 1748, 4132, 4413, 1891, 2143, 152, 3772, 721, 894, 4337, 2142, 2204, 2552, 294, 479, 1540, 408, 2315, 2720, 812, 2410, 605, 2948, 3936, 3716, 3728, 1085, 3515, 3352, 1292, 151, 798, 623, 1824, 1827, 238, 1471, 3125, 190, 1286, 3932, 3162, 377, 2274, 139, 3210, 1708, 2499, 2303, 2118, 3516, 2896, 3707, 906, 4415, 1614, 870, 4263, 1337, 2934, 1527, 3312, 3232, 1853, 192, 1163, 4032, 3142, 2543, 2147, 661, 727, 96, 1190, 2929, 1699, 3860, 49, 4277, 452, 1456, 1102, 1391, 165, 2469, 498, 588, 737, 1370, 1293, 1732, 1994, 2655, 3662, 2846, 4241, 2023, 3246, 1326, 3783, 2931, 146, 1032, 1684, 4482, 4309, 2356, 3615, 3436, 113, 1930, 4169, 396, 3588, 3438, 1856, 593, 3810, 959, 3944, 1549, 2247, 2424, 357, 3752, 2448, 4492, 1113, 4344, 4441, 1320, 2310, 136, 2877, 2359, 3237, 4445, 3537, 302, 1421, 3613, 2178, 2115, 1079, 1767, 2313, 1207, 1602, 3654, 2489, 3283, 1531, 2238, 874, 4130, 3991, 1959, 1123, 2554, 2349, 1055, 3554, 626, 3674, 4442, 2975, 3277, 3453, 4206, 1235, 327, 2802, 3224, 2557, 979, 2425, 3776, 1622, 4045, 3392, 3510, 3556, 3106, 3022, 3146, 4048, 1983, 3520, 2180, 1542, 4235, 3241, 3872, 1927, 2069, 1033, 807, 1440, 60, 2277, 2426, 1589, 241, 4027, 1343, 2225, 4391, 3527, 4488, 1339, 412, 3376, 2828, 425, 1044, 4318, 1917, 1922, 3896, 4367, 1762, 2707, 664, 1008, 2717, 3304, 1296, 3368, 677, 3502, 3057, 1409, 1705, 3431, 3297, 2130, 4363, 300, 2829, 3753, 3427, 3941, 2900, 1017, 329, 1850, 1742, 3403, 889, 4238, 488, 1323, 4118, 3821, 87, 255, 1111, 2162, 802, 212, 3523, 2345, 2969, 875, 1528, 3025, 1899, 4326, 2772, 2025, 1171, 795, 3530, 1248, 4434, 2505, 3863, 4255, 4370, 1247, 4355, 3889, 3879, 3998, 285, 2372, 3740, 764, 2014, 2949, 1995, 3139, 3244, 1727, 3831, 67, 3088, 2922, 1109, 951, 1965, 2830, 3013, 1, 364, 1270, 1463, 520, 901, 2676, 3152, 3764, 1897, 3281, 1451, 2187, 567, 2621, 3117, 3577, 1309, 2011, 1084, 3292, 3490, 3535, 944, 4062, 3323, 3455, 4123, 1525, 4213, 4096, 1342, 3812, 72, 3135, 492, 1665, 4203, 3874, 2285, 688, 4052, 2966, 1228, 3798, 2991, 230, 409, 3827, 1180, 3100, 949, 2070, 909, 1260, 2867, 1403, 4097, 2789, 1534, 3380, 293, 739, 692, 119, 2435, 1731, 3346, 1410, 3176, 1743, 1089, 474, 2779, 2753, 4412, 2697, 2526, 2677, 917, 4435, 1592, 1713, 1097, 4393, 2483, 3445, 1493, 4417, 3420, 582, 2153, 578, 3063, 4074, 3953, 1443, 1932, 1671, 4250, 651, 1729, 2626, 3846, 185, 3340, 383, 913, 4464, 19, 3706, 963, 4474, 3143, 845, 1305, 2354, 3650, 1182, 2783, 2525, 1329, 1958, 4059, 1321, 4346, 3353, 1212, 2041, 2571, 1889, 3549, 3568, 3525, 215, 2756, 154, 4331, 264, 3309, 3467, 3310, 1499, 2353, 1733, 1169, 1263, 82, 1766, 1635, 4428, 3379, 2599, 2458, 27, 3364, 1090, 3236, 1204, 3066, 3972, 4304, 4155, 713, 779, 1660, 3216, 2696, 2832, 372, 1276, 391, 2492, 3935, 1256, 4037, 1101, 3282, 571, 4362, 1566, 1769, 183, 1604, 1558, 3727, 3529, 966, 1505, 2471, 934, 3508, 2064, 1869, 2721, 4323, 4463, 106, 3800, 831, 1302, 3594, 3023, 1000, 3766, 3417, 642, 4102, 908, 2941, 4236, 2125, 3912, 1877, 2662, 1823, 645, 1601, 404, 794, 2438, 3141, 1556, 3591, 3158, 602, 3190, 3136, 1629, 2034, 2858, 635, 2196, 2959, 1300, 1164, 2977, 657, 4372, 200, 3324, 4456, 1924, 2963, 406, 4465, 4424, 2793, 1544, 1625, 2038, 1862, 3017, 1133, 513, 3541, 1430, 2627, 1136, 2566, 3036, 4401, 633, 1842, 2656, 530, 1789, 1916, 3544, 4073, 3617, 2018, 1887, 1919, 1232, 470, 2212, 3174, 2502, 2813, 4216, 1949, 125, 864, 2302, 777, 2550, 1569, 2678, 2638, 354, 3754, 1673, 3192, 235, 542, 2327, 122, 2791, 3779, 2421, 3909, 658, 2012, 3286, 2396, 3119, 1353, 1220, 265, 3904, 1324, 3620, 292, 4267, 437, 1016, 403, 2010, 3590, 3316, 1597, 3624, 2350, 253, 3595, 2542, 2725, 3471, 3072, 3175, 2150, 3828, 4115, 497, 2452, 367, 3054, 1045, 1612, 715, 186, 2500, 3394, 2989, 2447, 2129, 2631, 1939, 382, 2643, 1290, 3159, 3869, 1691, 65, 4374, 8, 1879, 3807, 2388, 1196, 1715, 2080, 4284, 401, 2363, 4024, 1934, 465, 550, 3741, 561, 3937, 1974, 1173, 2239, 2687, 2141, 3697, 4005, 4385, 2985, 3958, 726, 3840, 2321, 643, 1401, 1634, 557, 3050, 1405, 4083, 410, 180, 3715, 2202, 861, 2915, 3479, 1479, 2254, 3704, 478, 789, 1202, 2362, 3153, 199, 13, 1151, 648, 2074, 399, 3667, 3094, 2208, 3980, 814, 2536, 4035, 4294, 2718, 1892, 3934, 914, 3988, 749, 3027, 3661, 1830, 462, 2684, 1608, 3325, 4450, 24, 2776, 3913, 3732, 1081, 130, 1756, 1586, 290, 2973, 1229, 141, 3804, 2298, 73, 3150, 649, 456, 1316, 1947, 3320, 2248, 1751, 1529, 821, 559, 3307, 4228, 3378, 4044, 3703, 2919, 3531, 915, 1027, 783, 2798, 3987, 2360, 3201, 2029, 1986, 3770, 175, 3225, 3601, 3687, 2488, 3148, 2493, 4487, 859, 1087, 662, 655, 3300, 405, 1572, 4220, 4336, 373, 4301, 3900, 2031, 4182, 51, 967, 691, 449, 289, 4221, 3214, 4416, 1218, 2027, 1690, 2291, 3902, 772, 226, 4308, 3656, 595, 2774, 4186, 1861, 30, 1119, 885, 3660, 3908, 166, 1176, 4268, 2043, 1124, 2075, 2098, 2563, 4087, 1594, 4410, 1806, 1211, 2357, 2999, 1469, 1774, 3104, 1387, 2381, 1411, 1610, 4105, 2073, 2055, 1509, 2117, 2445, 950, 2715, 1725, 2261, 1395, 3971, 2912, 900, 3536, 2021, 3986, 394, 3460, 586, 3738, 1004, 2960, 305, 1444, 164, 2337, 536, 1613, 495, 2751, 927, 2572, 4373, 1458, 2956, 2402, 2976, 3663, 4184, 3362, 1504, 1288, 1797, 343, 504, 4327, 1936, 3351, 1047, 2113, 3127, 3034, 2704, 4025, 1025, 893, 3120, 3206, 159, 1048, 4396, 2288, 3599, 3059, 3769, 4378, 863, 3750, 515, 1478, 4218, 3711, 2610, 4108, 3107, 3960, 907, 4099, 3092, 2617, 1365, 1802, 1906, 1712, 2037, 1740, 3999, 1992, 3496, 1379, 1609, 3600, 4144, 2259, 3414, 494, 4408, 2260, 785, 3010, 4411, 2484, 2088, 1541, 3009, 1642, 1888, 2245, 2108, 3033, 150, 4339, 1383, 3995, 1723, 3546, 1940, 3830, 4251, 2097, 2558, 773, 1344, 3598, 92, 2598, 1941, 1306, 2220, 4013, 3627, 2000, 3923, 3435, 291, 4315, 2866, 4140, 2573, 4178, 518, 1730, 3164, 2393, 2336, 2806, 131, 4078, 2815, 792, 3430, 4137, 4281, 3180, 3746, 3425, 2529, 3474, 57, 2411, 2215, 4473, 378, 4419, 453, 1303, 1780, 3690, 464, 4188, 1480, 137, 4402, 667, 4153, 4011, 884, 2671, 2312, 1650, 1648, 2586, 2331, 2093, 2355, 10, 2319, 3718, 4006, 975, 2987, 4300, 4292, 1517, 1591, 3636, 4000, 2953, 834, 1142, 1999, 1422, 3839, 3363, 531, 781, 1896, 3409, 1776, 2530, 3332, 3295, 4376, 2223, 423, 1679, 2230, 1790, 2326, 1786, 594, 2217, 3884, 1148, 2058, 3619, 1002, 3046, 1147, 4381, 2538, 1268, 1143, 3538, 3569, 35, 2851, 1718, 475, 1905, 2661, 2601, 2155, 1506, 872, 102, 1580, 868, 1277, 314, 3948, 4128, 4030, 3709, 14, 2757, 2607, 4459, 26, 2376, 1406, 3218, 2819, 1289, 624, 1828, 3260, 3327, 3825, 3835, 2299, 529, 88, 398, 3997, 3774, 2605, 650, 3745, 1330, 1644, 539, 142, 3049, 55, 1619, 2454, 2845, 1944, 2766, 1664, 3855, 4003, 3672, 3195, 163, 1258, 2705, 2409, 105, 1099, 4021, 3733, 2047, 402, 3566, 3587, 4232, 3883, 3075, 965, 2269, 2786, 905, 3781, 1366, 3356, 4038, 77, 3726, 670, 2146, 1501, 2980, 1980, 4240, 1390, 1770, 1162, 1115, 1885, 895, 31, 2380, 1925, 310, 2459, 660, 543, 2040, 2532, 3410, 3543, 2510, 1009, 1128, 2818, 2692, 2585, 3956, 4164, 1915, 3622, 4290, 3539, 596, 3302, 686, 4110, 2770, 2630, 2442, 3211, 268, 172, 3626, 313, 2879, 3313, 4305, 4483, 2833, 1945, 2986, 3790, 2834, 272, 4341, 3035, 3870, 4256, 349, 1593, 3157, 2134, 3073, 4147, 3881, 3498, 3070, 2658, 1476, 2906, 4107, 1490, 3686, 2540, 1408, 828, 1437, 4199, 1082, 48, 4008, 3405, 2138, 1282, 618, 1649, 1883, 2227, 683, 1255, 4313, 3126, 334, 356, 2968, 835, 2216, 3442, 1704, 145, 2932, 1492, 2731, 2636, 1325, 3842, 3666, 2340, 3901, 2407, 1294, 1779, 2103, 3669, 4335, 2369, 4208, 2659, 3443, 936, 3167, 2320, 2271, 622, 2199, 2066, 2389, 1035, 2207, 2307, 538, 3299, 2279, 3589, 1918, 2982, 2330, 3369, 232, 2926, 2406, 2515, 748, 4431, 1687, 971, 829, 4, 3273, 929, 1627, 1988, 2222, 4371, 3967, 2611, 283, 3386, 3319, 675, 1224, 4185, 2835, 757, 3676, 1098, 990, 3801, 3743, 1512, 883, 4380, 109, 2814, 3691, 516, 1466, 387, 4310, 390, 2487, 2339, 2449, 1697, 4478, 592, 2875, 1857, 221, 4171, 3197, 4418, 947, 214, 689, 3470, 2654, 4260, 2470, 1037, 790, 250, 3355, 4497, 3757, 3256, 2456, 1106, 2517, 2712, 3675, 3651, 2149, 3484, 4091, 3808, 4500, 3572, 2904, 3291, 2914, 899, 3276, 1588, 1881, 604, 4064, 143, 1923, 4034, 3081, 1489, 3477, 460, 2673, 2826, 2907, 4245, 1287, 1902, 1246, 4217, 2286, 3280, 2990, 3426, 85, 4172, 1784, 1252, 469, 3068, 346, 765, 3829, 849, 1011, 4425, 4343, 2136, 1624, 1198, 1022, 1716, 2473, 1621, 2556, 886, 2171, 3949, 4167, 3391, 461, 2564, 811, 2609, 4320, 2006, 319, 607, 270, 923, 244, 1291, 1120, 3372, 2062, 2681, 1076, 3861, 1855, 473, 3390, 445, 3311, 3130, 415, 217, 3478, 1397, 2902, 2019, 1524, 1893, 1250, 3684, 2151, 2139, 3084, 3560, 1364, 256, 2266, 911, 3975, 2771, 1061, 350, 2763, 887, 121, 4306, 3082, 0, 322, 1669, 523, 3951, 654, 2156, 3018, 1374, 476, 3006, 4201, 613, 1368, 1284, 1598, 4295, 4299, 921, 2646, 1088, 4395, 505, 3799, 1483, 295, 718, 3005, 956, 775, 1783, 68, 2482, 3491, 528, 2629, 1545, 247, 4271, 3593, 742, 1518, 4476, 3170, 3847, 4029, 563, 3341, 768, 2546, 4384, 2874, 827, 3263, 2891, 1872, 922, 848, 3963, 2921, 3089, 1709, 533, 2993, 2441, 2003, 2, 3097, 1503, 4484, 4328, 805, 1468, 1787, 4394, 4135, 3193, 1989, 1692, 3634, 3749, 2674, 4493, 738, 3796, 4254, 3007, 195, 2527, 4234, 120, 2035, 1680, 1279, 619, 220, 3459, 79, 1696, 3678, 483, 1737, 4197, 3318, 3343, 1186, 2154, 2792, 338, 1636, 3015, 3102, 325, 4122, 3270, 2521, 3336, 76, 754, 1873, 2895, 2823, 1633, 1253, 2287, 1693, 2284, 2569, 1210, 4283, 3653, 110, 2159, 1734, 3926, 2121, 2612, 3473, 3132, 3123, 3488, 957, 153, 4244, 2595, 3284, 2514, 978, 4253, 3608, 672, 3942, 2167, 3983, 4222, 348, 1552, 3262, 3199, 3289, 997, 1145, 20, 2002, 1418, 318, 669, 3000, 519, 556, 3494, 2309, 1753, 652, 419, 306, 2366, 1398, 84, 3513, 234, 3101, 1714, 3219, 3834, 4471, 638, 1775, 674, 328, 3604, 4049, 2092, 1127, 2995, 1245, 1811, 2004, 3763, 1117, 169, 3606, 2568, 1804, 3458, 281, 3056, 3269, 2909, 23, 3497, 3429, 1261, 839, 4469, 838, 3048, 155, 2281, 1157, 1668, 852, 3826, 1046, 3245, 2928, 3655, 1781, 1096, 3865, 116, 1967, 2694, 2278, 579, 2635, 2920, 3151, 2693, 3287, 668, 1747, 1706, 1018, 2587, 4243, 517, 4322, 1013, 1677, 434, 3156, 303, 4342, 2642, 4170, 489, 3966, 3914, 890, 3729, 2957, 4014, 3194, 1470, 2785, 2398, 3188, 278, 4458, 2422, 2997, 756, 1135, 193, 825, 766, 2242, 2945, 1372, 53, 2429, 369, 1003, 335, 2124, 780, 2179, 2974, 1623, 2262, 1086, 3374, 4479, 4364, 4090, 1053, 2938, 2562, 2213, 4010, 1674, 3918, 524, 274, 2335, 4443, 81, 1328, 3044, 467, 1134, 4246, 731, 958, 2461, 3191, 3702, 63, 249, 2873, 3357, 179, 1020, 2582, 945, 429, 2255, 2849, 873, 3345, 808, 336, 3542, 1413, 4225, 1450, 846, 2273, 2588, 743, 2119, 2433, 2575, 4022, 3401, 968, 3111, 3773, 1114, 2782, 29, 1972, 358, 4086, 3177, 4131, 2341, 3382, 1193, 502, 3421, 2972, 2688, 2865, 1655, 2699, 3845, 2551, 2864, 2548, 508, 4451, 3924, 2229, 2079, 1122, 3469, 2935, 1299, 1859, 2574, 1607, 2709, 2861, 2734, 1361, 3388, 2280, 1230, 45, 1744, 1532, 3522, 1555, 3823, 157, 3849, 3780, 910, 1618, 3639, 197, 3424, 565, 2127, 4475, 1741, 2730, 1226, 4154, 275, 2506, 989, 38, 2683, 1746, 3984, 4055, 3149, 3160, 606, 3748, 2501, 3734, 584, 3008, 3124, 3555, 1338, 330, 4149, 3128, 4012, 931, 4112, 297, 3609, 4195, 1249, 3428, 3228, 1121, 3045, 1057, 3155, 3203, 2691, 1568, 317, 1197, 59, 3333, 3905, 3483, 1817, 2899, 1063, 2203, 3305, 2334, 435, 4207, 463, 548, 3272, 2065, 3492, 39, 388, 1750, 2101, 903, 2346, 4046, 2293, 942, 3817, 2597, 2228, 2297, 3476, 2082, 2578, 1051, 3373, 1868, 1314, 1860, 472, 4060, 3784, 3818, 2292, 1759, 1583, 1581, 3581, 1795, 3012, 1116, 1350, 128, 711, 2110, 3495, 2193, 2943, 3342, 857, 3621, 3771, 512, 2295, 3532, 269, 4386, 1156, 3114, 3815, 1030, 147, 4269, 3873, 2860, 3906, 1404, 4379, 1213, 1526, 3294, 3030, 3893, 609, 2992, 3685, 83, 2565, 3820, 3969, 2241, 2592, 4369, 252, 1630, 2807, 1146, 1189, 2104, 4481, 3131, 855, 2898, 42, 2085, 1895, 1464, 480, 1160, 3266, 344, 3451, 1956, 3163, 1373, 3584, 2111, 3449, 2561, 1356, 4039, 521, 3747, 2170, 3016, 4325, 1067, 362, 3648, 2841, 132, 1060, 1317, 4462, 94, 203, 1845, 1502, 1477, 509, 176, 4036, 3338, 2876, 3803, 3406, 2444, 2211, 3638, 1508, 3215, 257, 510, 1771, 2189, 4156, 3011, 2836, 4249, 3633, 1982, 2017, 1914, 259, 1358, 2726, 3657, 3689, 2371, 1452, 1125, 3040, 1112, 1682, 2871, 2076, 2437, 2886, 2099, 2722, 1812, 3762, 1984, 2735, 2553, 1388, 2026, 3629, 4359, 3857, 3328, 3419, 1948, 3169, 3234, 2385, 1929, 4266, 976, 1931, 1396, 4286, 3680, 4273, 3788, 1521, 2301, 3418, 1843, 2490, 3456, 2186, 526, 2996, 420, 1414, 430, 1092, 728, 1040, 2126, 3785, 2071, 3238, 2289, 433, 2008, 1912, 2377, 1177, 187, 3628, 740, 549, 2769, 3475, 3886, 114, 3259, 1153, 393, 937, 995, 158, 1722, 1530, 2131, 44, 4382, 1105, 3024, 4340, 4227, 1663, 1578, 3361, 2644, 1462, 3161, 4106, 2522, 3517, 3404, 983, 2950, 644, 3692, 21, 3806, 2057, 2039, 3929, 3551, 2535, 4297, 1118, 219, 32, 340, 3930, 2478, 2885, 745, 1225, 1848, 1072, 2664, 3658, 4033, 1185, 4017, 2201, 1533, 1515, 823, 2176, 93, 2128, 1548, 1735, 2072, 3069, 673, 1810, 1620, 2342, 99, 1138, 2940, 363, 202, 1867, 3576, 880, 3301, 2710, 365, 4148, 2971, 1874, 2249, 3037, 2466, 2328, 2787, 3545, 1685, 1539, 4214, 841, 2839, 1798, 628, 755, 3257, 1415, 3503, 3331, 3720, 307, 3895, 1961, 124, 3138, 3898, 4491, 746, 3489, 34]

import re
import string

import matplotlib.pyplot as plt
import nltk
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
import json


def getStatsFromModel(model, X_test, y_test, y_pred):
    print(classification_report(y_test, y_pred))


def classifyPhaseOne(url):
    df = pd.read_json(url, lines=True, orient='columns')

    for i in range(0, len(df)):
        if df.annotation[i]['label'][0] == '1':
            df.annotation[i] = 1
        else:
            df.annotation[i] = 0

    df.drop(['extras'], axis=1, inplace=True)
    df['annotation'].value_counts().sort_index().plot.bar()

    # Biasness
    print("Positive non cybertrolling: ", df.annotation.value_counts()[0] / len(df.annotation) * 100, "%")
    print("Cybertrolling: ", df.annotation.value_counts()[1] / len(df.annotation) * 100, "%")

    nltk.download('stopwords')
    stop = stopwords.words('english')

    regex = re.compile('[%s]' % re.escape(string.punctuation))

    def test_re(s):
        return regex.sub('', s)

    df['content_without_stopwords'] = df['content'].apply(
        lambda x: ' '.join([word for word in x.split() if word not in stop]))
    df['content_without_puncs'] = df['content_without_stopwords'].apply(lambda x: regex.sub('', x))
    del df['content_without_stopwords']
    del df['content']

    # Stemming
    porter_stemmer = PorterStemmer()
    # punctuations
    nltk.download('punkt')
    tok_list = []
    size = df.shape[0]

    for i in range(size):
        word_data = df['content_without_puncs'][i]
        nltk_tokens = nltk.word_tokenize(word_data)
        final = ''
        for w in nltk_tokens:
            final = final + ' ' + porter_stemmer.stem(w)
        tok_list.append(final)

    df['content_tokenize'] = tok_list
    del df['content_without_puncs']

    noNums = []
    for i in range(len(df)):
        noNums.append(''.join([i for i in df['content_tokenize'][i] if not i.isdigit()]))

    df['content'] = noNums

    tfIdfVectorizer = TfidfVectorizer(use_idf=True, sublinear_tf=True)
    tfIdf = tfIdfVectorizer.fit_transform(df.content.tolist())
    dfx = pd.DataFrame(tfIdf.toarray(), columns=tfIdfVectorizer.get_feature_names())

    X = tfIdf.toarray()
    y = np.array(df.annotation.tolist())

    # Splitting
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Training data biasness
    unique_elements, counts_elements = np.unique(y_train, return_counts=True)
    print(np.asarray((unique_elements, counts_elements)))

    # Test Data
    unique_elements, counts_elements = np.unique(y_test, return_counts=True)
    print(np.asarray((unique_elements, counts_elements)))

    # Random oversampling on training data

    oversample = RandomOverSampler(sampling_strategy='not majority')
    X_over, y_over = oversample.fit_resample(X_train, y_train)

    unique_elements, counts_elements = np.unique(y_over, return_counts=True)
    print(np.asarray((unique_elements, counts_elements)))

    rfc = RandomForestClassifier(verbose=True)  # uses randomized decision trees
    rfcmodel = rfc.fit(X_over, y_over)
    y_pred = rfc.predict(X_test)
    print("Score:", rfcmodel.score(X_test, y_test))
    print("Confusion Matrix: \n", confusion_matrix(y_test, y_pred))
    getStatsFromModel(rfc, X_test, y_test, y_pred)

    return rfc, df.query("annotation == 1"), tfIdfVectorizer


def classifyPhaseTwo(hateComments):
    tfIdfVectorizer = TfidfVectorizer(use_idf=True, sublinear_tf=True)
    tfIdf = tfIdfVectorizer.fit_transform(hateComments.content.tolist())

    dfx = pd.DataFrame(tfIdf.toarray(), columns=tfIdfVectorizer.get_feature_names())
    X = tfIdf.toarray()
    y = np.array(hateComments.severity.tolist())

    # Splitting
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

    # Training data biasness
    unique_elements, counts_elements = np.unique(y_train, return_counts=True)
    print(np.asarray((unique_elements, counts_elements)))

    # Test Data
    unique_elements, counts_elements = np.unique(y_test, return_counts=True)
    print(np.asarray((unique_elements, counts_elements)))

    # Random oversampling on training data
    oversample = RandomOverSampler(sampling_strategy='not majority')
    X_over, y_over = oversample.fit_resample(X_train, y_train)

    rfc = RandomForestClassifier(verbose=True)  # uses randomized decision trees
    rfcmodel = rfc.fit(X_over, y_over)
    y_pred = rfc.predict(X_test)
    print("Score:", rfcmodel.score(X_test, y_test))
    print("Confusion Matrix: \n", confusion_matrix(y_test, y_pred))
    getStatsFromModel(rfc, X_test, y_test, y_pred)
    return rfc, tfIdfVectorizer

def preprocess(comment):
    stop = stopwords.words('english')

    regex = re.compile('[%s]' % re.escape(string.punctuation))
    comment = ' '.join([word for word in comment.split() if word not in stop])
    comment = regex.sub('', comment)

    # Stemming
    porter_stemmer = PorterStemmer()
    # punctuations
    nltk.download('punkt')
    comment = ' '.join([porter_stemmer.stem(word) for word in comment.split() if word not in stop])
    comment = ''.join([i for i in comment if not i.isdigit()])

    return comment

model, hateComments, hateVectorizer = classifyPhaseOne('dataset.json')
rfc, vectorizer = classifyPhaseTwo(hateComments)

@app.route('/')
def dummy():
    return {}


final = []
# Route for seeing a data
@app.route('/data')
def get_comments():
    global final

    if not final:
        file = open("dataset.json", "r")
        s = file.readlines()
        comments = [json.loads(i) for i in s]

        for i in comments:
            if i['annotation']['label'][0] == '1':
                i['hate'] = 1
            else:
                i['hate'] = 0

        for i in index:
            final += comments[i],
    
    return final[::-1]
  
@app.route('/add_comment', methods=['POST'])
def add_comment():
    global final

    comment = request.get_json()
    processed_comment = hateVectorizer.transform([preprocess(comment['content'])])
    
    hate = model.predict(processed_comment)[0]
    if hate:
        comment['hate'] = '1'
        processed_comment = vectorizer.transform([preprocess(comment['content'])])
        comment['severity'] = str(rfc.predict(processed_comment)[0])
    else:
        comment['hate'] = '0'
        comment['severity'] = '0'

    print(comment)
    final += comment,
    return 'Done', 201

# Running app
if __name__ == '__main__':
    app.run(debug=True)