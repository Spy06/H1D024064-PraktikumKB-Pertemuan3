import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

kejelasan_informasi = ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_informasi')
kejelasan_persyaratan= ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_persyaratan')
kemampuan_petugas= ctrl.Antecedent(np.arange(0, 101, 1), 'kemampuan_petugas')
ketersediaan_fasilitas = ctrl.Antecedent(np.arange(0, 101, 1), 'ketersediaan_fasilitas')
kepuasan_pelayanan = ctrl.Consequent(np.arange(0, 401, 1), 'kepuasan_pelayanan')

kejelasan_informasi['tidak memuaskan'] = fuzz.trapmf(kejelasan_informasi.universe, [0, 0, 60,75])
kejelasan_informasi['cukup memuaskan'] = fuzz.trimf(kejelasan_informasi.universe, [60, 75, 90])
kejelasan_informasi['memuaskan'] = fuzz.trapmf(kejelasan_informasi.universe, [75, 90, 100,100]) # Corrected typo here

kejelasan_persyaratan['tidak memuaskan'] = fuzz.trapmf(kejelasan_persyaratan.universe, [0, 0, 60,75])
kejelasan_persyaratan['cukup memuaskan'] = fuzz.trimf(kejelasan_persyaratan.universe, [60, 75, 90])
kejelasan_persyaratan['memuaskan'] = fuzz.trapmf(kejelasan_persyaratan.universe, [75, 90, 100,100])

kemampuan_petugas['tidak memuaskan'] = fuzz.trapmf(kemampuan_petugas.universe, [0, 0, 60,75])
kemampuan_petugas['cukup memuaskan'] = fuzz.trimf(kemampuan_petugas.universe, [60, 75, 90])
kemampuan_petugas['memuaskan'] = fuzz.trapmf(kemampuan_petugas.universe, [75, 90, 100,100])

ketersediaan_fasilitas['tidak memuaskan'] = fuzz.trapmf(ketersediaan_fasilitas.universe, [0, 0, 60,75])
ketersediaan_fasilitas['cukup memuaskan'] = fuzz.trimf(ketersediaan_fasilitas.universe, [60, 75, 90])
ketersediaan_fasilitas['memuaskan'] = fuzz.trapmf(ketersediaan_fasilitas.universe, [75, 90, 100,100])

kepuasan_pelayanan['tidak memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [0, 0, 50,75])
kepuasan_pelayanan['kurang memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [50, 75, 100,150])
kepuasan_pelayanan['cukup memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [100, 150, 250,275])
kepuasan_pelayanan['memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [250, 275, 325,350])
kepuasan_pelayanan['sangat memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [325, 350,400,400])

aturan1 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['kurang memuaskan'])
aturan2 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan3 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan4 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan5 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan6 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan7 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan8 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan9 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan10 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan11 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan12 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan13 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan14 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan15 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan16 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan17 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan18 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan19 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan20 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan21 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan22 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan23 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan24 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan25 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan26 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan27 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan28 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan29 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan30 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan31 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan32 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan33 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan34 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan35 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan36 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan37 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan38 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan39 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan40 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan41 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan42 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan43 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan44 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan45 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan46 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan47 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan48 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan49 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan50 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan51 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan52 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan53 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan54 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan55 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan56 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan57 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan58 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan59 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan60 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan61 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan62 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan63 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan64 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan65 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan66 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan67 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan68 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan69 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan70 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan71 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan72 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan73 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan74 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan75 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan76 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan77 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan78 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan79 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['tidak memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan80 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['cukup memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan81 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_fasilitas['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])

sistem_kepuasan = ctrl.ControlSystem([
aturan1, aturan2, aturan3, aturan4, aturan5, aturan6, aturan7, aturan8, aturan9,
aturan10, aturan11, aturan12, aturan13, aturan14, aturan15, aturan16, aturan17, aturan18,
aturan19, aturan20, aturan21, aturan22, aturan23, aturan24, aturan25, aturan26, aturan27,
aturan28, aturan29, aturan30, aturan31, aturan32, aturan33, aturan34, aturan35, aturan36,
aturan37, aturan38, aturan39, aturan40, aturan41, aturan42, aturan43, aturan44, aturan45,
aturan46, aturan47, aturan48, aturan49, aturan50, aturan51, aturan52, aturan53, aturan54,
aturan55, aturan56, aturan57, aturan58, aturan59, aturan60, aturan61, aturan62, aturan63,
aturan64, aturan65, aturan66, aturan67, aturan68, aturan69, aturan70, aturan71, aturan72,
aturan73, aturan74, aturan75, aturan76, aturan77, aturan78, aturan79, aturan80, aturan81
])
simulasi_kepuasan = ctrl.ControlSystemSimulation(sistem_kepuasan)

simulasi_kepuasan.input['kejelasan_informasi'] = 80
simulasi_kepuasan.input['kejelasan_persyaratan'] = 60
simulasi_kepuasan.input['kemampuan_petugas'] = 50
simulasi_kepuasan.input['ketersediaan_fasilitas'] = 90

simulasi_kepuasan.compute()

hasil_kepuasan = simulasi_kepuasan.output['kepuasan_pelayanan']
print("--- HASIL PERHITUNGAN LOGIKA FUZZY ---")
print(f"Kejelasan Informasi : 80")
print(f"Kejelasan Persyaratan : 60")
print(f"Kemampuan petugas : 50")
print(f"ketersediaan sarpras : 90")
print("--------------------------------------")
print(f"kepuasan pelayanan: {hasil_kepuasan:.2f} unit")

kejelasan_informasi.view(sim=simulasi_kepuasan)
kejelasan_persyaratan.view(sim=simulasi_kepuasan)
kemampuan_petugas.view(sim=simulasi_kepuasan)
ketersediaan_fasilitas.view(sim=simulasi_kepuasan)
kepuasan_pelayanan.view()