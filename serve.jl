#!/usr/bin/env julia

using Pkg
Pkg.activate("emat10006")
Pkg.add("Franklin")
using Franklin
serve()
