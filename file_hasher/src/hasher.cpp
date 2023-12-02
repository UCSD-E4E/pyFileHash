#include <fstream>
#include <iostream>
#include <string>

#include <pybind11/pybind11.h>
#include "hash-library/hash.h"

typedef enum HashType {
    CRC32 = 0,
    MD5,
    SHA1,
    SHA256,
    SHA3
}Hash_t;


std::string compute_digest(Hash_t hash_type, std::string path)
{
    std::fstream handle;
    handle.open(path);
    if (!handle.is_open())
    {
        throw std::exception("Unable to open file");
    }
    handle.close();
    return std::string(path);
}

namespace py = pybind11;
PYBIND11_MODULE(file_hasher, m) {
    py::enum_<HashType>(m, "HashType")
        .value("CRC32", CRC32)
        .value("MD5", MD5)
        .value("SHA1", SHA1)
        .value("SHA256", SHA256)
        .export_values();
    m.def("compute_digest", &compute_digest);
}