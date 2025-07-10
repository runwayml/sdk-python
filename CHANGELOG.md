# Changelog

## 3.6.4 (2025-07-10)

Full Changelog: [v3.6.3...v3.6.4](https://github.com/runwayml/sdk-python/compare/v3.6.3...v3.6.4)

### Bug Fixes

* **parsing:** correctly handle nested discriminated unions ([813daf2](https://github.com/runwayml/sdk-python/commit/813daf265fdd93af5500a1b7cf2c7def33f31e08))

## 3.6.3 (2025-07-09)

Full Changelog: [v3.6.2...v3.6.3](https://github.com/runwayml/sdk-python/compare/v3.6.2...v3.6.3)

### Chores

* **internal:** bump pinned h11 dep ([25ee0aa](https://github.com/runwayml/sdk-python/commit/25ee0aadb87786a3825169c3e84cc80398188ba5))
* **package:** mark python 3.13 as supported ([b50298a](https://github.com/runwayml/sdk-python/commit/b50298a999f71b7ce49e640eac691ca71ee39135))

## 3.6.2 (2025-07-08)

Full Changelog: [v3.6.1...v3.6.2](https://github.com/runwayml/sdk-python/compare/v3.6.1...v3.6.2)

### Bug Fixes

* **ci:** correct conditional ([04df1e3](https://github.com/runwayml/sdk-python/commit/04df1e3c225dcfa89036bdbdc8dbe3fd3f0f6233))
* **ci:** release-doctor — report correct token name ([5c77b20](https://github.com/runwayml/sdk-python/commit/5c77b20928d41e78f6b67136ebf6236078d3669b))


### Chores

* **ci:** change upload type ([1ca0a49](https://github.com/runwayml/sdk-python/commit/1ca0a49d43c99e8aa90b5781eb5a530f6a7038bb))
* **ci:** only run for pushes and fork pull requests ([0821c24](https://github.com/runwayml/sdk-python/commit/0821c241c8364476413df18c1af16b95556c187f))
* **internal:** codegen related update ([cfd7b38](https://github.com/runwayml/sdk-python/commit/cfd7b3830de1d53d5b55aecec5dc947851a26d04))

## 3.6.1 (2025-06-24)

Full Changelog: [v3.6.0...v3.6.1](https://github.com/runwayml/sdk-python/compare/v3.6.0...v3.6.1)

### Chores

* **tests:** skip some failing tests on the latest python versions ([732236d](https://github.com/runwayml/sdk-python/commit/732236d2ced9511c21179e9850bafcaf0b0a4edf))

## 3.6.0 (2025-06-23)

Full Changelog: [v3.5.0...v3.6.0](https://github.com/runwayml/sdk-python/compare/v3.5.0...v3.6.0)

### Features

* **client:** add support for aiohttp ([7d5490c](https://github.com/runwayml/sdk-python/commit/7d5490ca015dd0ff55789889036cc1bd32a58c43))


### Bug Fixes

* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([33301dd](https://github.com/runwayml/sdk-python/commit/33301ddf84cc64581d715d6b8ce1eda48ff66ed5))


### Chores

* **readme:** update badges ([147dc95](https://github.com/runwayml/sdk-python/commit/147dc95f9ab390065ab96403a88ca5a87e59f597))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([af9fecb](https://github.com/runwayml/sdk-python/commit/af9fecb38a4075fcc8f7687f2ef130ad8c813389))

## 3.5.0 (2025-06-17)

Full Changelog: [v3.4.0...v3.5.0](https://github.com/runwayml/sdk-python/compare/v3.4.0...v3.5.0)

### Features

* **api:** SDK updates, contentModeration for i2v ([1286e32](https://github.com/runwayml/sdk-python/commit/1286e3239f388143404c4b0a61816f5f6282fe1c))
* **api:** SDK updates, contentModeration for i2v ([8ff202e](https://github.com/runwayml/sdk-python/commit/8ff202ee39dc5856118bf1f3f5537e459a120967))


### Bug Fixes

* **client:** correctly parse binary response | stream ([fc9bedb](https://github.com/runwayml/sdk-python/commit/fc9bedb3cbb47849e83a5982ed92a694796e80c7))


### Chores

* **ci:** enable for pull requests ([4b439c9](https://github.com/runwayml/sdk-python/commit/4b439c99012918849be4fa64b1ab8d1802cee6e6))
* **internal:** update conftest.py ([0ff71fd](https://github.com/runwayml/sdk-python/commit/0ff71fd67a421dbff729e98418b6cd72ed0e57b3))
* **tests:** add tests for httpx client instantiation & proxies ([89e5fbe](https://github.com/runwayml/sdk-python/commit/89e5fbef9e8a64d050252f489b2d76e4c510c663))
* **tests:** run tests in parallel ([7edbcd1](https://github.com/runwayml/sdk-python/commit/7edbcd1db04ed139e026701fe24501199b4eaffd))

## 3.4.0 (2025-06-04)

Full Changelog: [v3.3.0...v3.4.0](https://github.com/runwayml/sdk-python/compare/v3.3.0...v3.4.0)

### Features

* **api:** Add video upscale endpoint ([aac6a70](https://github.com/runwayml/sdk-python/commit/aac6a707ca2925034fa141ceac8a9515958a77c1))

## 3.3.0 (2025-06-04)

Full Changelog: [v3.2.0...v3.3.0](https://github.com/runwayml/sdk-python/compare/v3.2.0...v3.3.0)

### Features

* **client:** add follow_redirects request option ([742ca3b](https://github.com/runwayml/sdk-python/commit/742ca3bbd1f38ce28ef26ddee06d4c86cd2a6ff0))


### Bug Fixes

* **docs:** fix confusing example in README ([54904f7](https://github.com/runwayml/sdk-python/commit/54904f7ed5557b5b3972fc25d52ffc873d91be7e))


### Chores

* **docs:** remove reference to rye shell ([e207562](https://github.com/runwayml/sdk-python/commit/e207562118ec1583e90639bbfc6cea00f4bed138))
* **docs:** remove unnecessary param examples ([d1ca063](https://github.com/runwayml/sdk-python/commit/d1ca06303f764543beda582da567ad182f25cf86))

## 3.2.0 (2025-05-29)

Full Changelog: [v3.1.0...v3.2.0](https://github.com/runwayml/sdk-python/compare/v3.1.0...v3.2.0)

### Features

* **api:** Add 720p t2i ratios ([b722686](https://github.com/runwayml/sdk-python/commit/b722686c0e4fa03768ce61380c77fe04c93cfc90))


### Chores

* **docs:** grammar improvements ([fbf2481](https://github.com/runwayml/sdk-python/commit/fbf2481cd6da85fb5ce2e6fea66cf8f1233a8e2e))

## 3.1.0 (2025-05-16)

Full Changelog: [v3.0.6...v3.1.0](https://github.com/runwayml/sdk-python/compare/v3.0.6...v3.1.0)

### Features

* **api:** Gen-4 Image (text-to-image) support ([8adcf96](https://github.com/runwayml/sdk-python/commit/8adcf96fa228c8694272175317587bf3c7b9e2fe))


### Chores

* **ci:** fix installation instructions ([a04350d](https://github.com/runwayml/sdk-python/commit/a04350dd31c9551695c1856a7f6d700d69960807))

## 3.0.6 (2025-05-15)

Full Changelog: [v3.0.5...v3.0.6](https://github.com/runwayml/sdk-python/compare/v3.0.5...v3.0.6)

### Chores

* **ci:** upload sdks to package manager ([23f0756](https://github.com/runwayml/sdk-python/commit/23f0756b5a8828ffa8477c51275df65f390193a7))

## 3.0.5 (2025-05-10)

Full Changelog: [v3.0.4...v3.0.5](https://github.com/runwayml/sdk-python/compare/v3.0.4...v3.0.5)

### Bug Fixes

* **package:** support direct resource imports ([f317064](https://github.com/runwayml/sdk-python/commit/f3170641fd7e8a58bfc8135314407e887a3a0068))


### Chores

* **internal:** avoid errors for isinstance checks on proxies ([a549b98](https://github.com/runwayml/sdk-python/commit/a549b98239afa6984f306db53cd2ac4895a7f4ac))

## 3.0.4 (2025-04-30)

Full Changelog: [v3.0.3...v3.0.4](https://github.com/runwayml/sdk-python/compare/v3.0.3...v3.0.4)

### Bug Fixes

* **api:** Fix for parameters with missing descriptions ([1ab27c6](https://github.com/runwayml/sdk-python/commit/1ab27c6285263701b69ed1ea05751a78a333e25f))
* **api:** Make `ratio` a required parameter for i2v ([e1b73a5](https://github.com/runwayml/sdk-python/commit/e1b73a55073ae5d0d224b751726515d946a93607))

## 3.0.3 (2025-04-24)

Full Changelog: [v3.0.2...v3.0.3](https://github.com/runwayml/sdk-python/compare/v3.0.2...v3.0.3)

### Bug Fixes

* **pydantic v1:** more robust ModelField.annotation check ([1f45aa4](https://github.com/runwayml/sdk-python/commit/1f45aa4ab023db52bc79a33492c4441f00d30d17))


### Chores

* broadly detect json family of content-type headers ([7adcad9](https://github.com/runwayml/sdk-python/commit/7adcad916636065b709d0bdff9c00047f48cf167))
* **ci:** add timeout thresholds for CI jobs ([a59f6e6](https://github.com/runwayml/sdk-python/commit/a59f6e62adc33fe07b81088f9ed066fd06118f63))
* **ci:** only use depot for staging repos ([bdd8635](https://github.com/runwayml/sdk-python/commit/bdd8635b236ca1686047d382f271e8a4954bc302))
* **internal:** codegen related update ([6ec7118](https://github.com/runwayml/sdk-python/commit/6ec7118bb5e1d1737d42cb017e2c8b133aa471d0))
* **internal:** fix list file params ([c745a86](https://github.com/runwayml/sdk-python/commit/c745a864dd1edcdc3ac38645963075e672723874))
* **internal:** import reformatting ([a991a2d](https://github.com/runwayml/sdk-python/commit/a991a2d2ac36ee544470999eeef0fe536b040b62))
* **internal:** minor formatting changes ([0f34a44](https://github.com/runwayml/sdk-python/commit/0f34a44ec0ee863d00e7656e7675ab43aa9ef973))
* **internal:** refactor retries to not use recursion ([b5637fb](https://github.com/runwayml/sdk-python/commit/b5637fbfc50816122689694ed2e0acef3020da03))
* **internal:** update models test ([79488d6](https://github.com/runwayml/sdk-python/commit/79488d6e50b1075d8f7cad6e3fb3ed022332e42e))

## 3.0.2 (2025-04-17)

Full Changelog: [v3.0.1...v3.0.2](https://github.com/runwayml/sdk-python/compare/v3.0.1...v3.0.2)

### Chores

* **internal:** base client updates ([6d4d8bb](https://github.com/runwayml/sdk-python/commit/6d4d8bb73df9c0985d12d349d783188de0cd7d7d))
* **internal:** bump pyright version ([5693e26](https://github.com/runwayml/sdk-python/commit/5693e261dcbc21f6a900c514ba8e6659e0a2cd4f))

## 3.0.1 (2025-04-15)

Full Changelog: [v3.0.0...v3.0.1](https://github.com/runwayml/sdk-python/compare/v3.0.0...v3.0.1)

### Bug Fixes

* **perf:** optimize some hot paths ([0c187d1](https://github.com/runwayml/sdk-python/commit/0c187d1c445dd39661ec91f809ba1e51a9b5f0f2))
* **perf:** skip traversing types for NotGiven values ([a65d4b0](https://github.com/runwayml/sdk-python/commit/a65d4b0375c412d1b707550a8e1b1d9ba9319130))


### Chores

* **client:** minor internal fixes ([09dd17f](https://github.com/runwayml/sdk-python/commit/09dd17fc639bc5c9aadfc033c131b133764d4e5b))
* **internal:** expand CI branch coverage ([8bde5ff](https://github.com/runwayml/sdk-python/commit/8bde5ff981d4acd0696ad3b7ac778ca21a49a8ac))
* **internal:** reduce CI branch coverage ([5892e7a](https://github.com/runwayml/sdk-python/commit/5892e7aa93fa9e091f111fd0590b239487ba61eb))
* **internal:** update pyright settings ([8b3a8ae](https://github.com/runwayml/sdk-python/commit/8b3a8ae32a589680549054328996ae7314be3033))

## 3.0.0 (2025-04-09)

Full Changelog: [v2.3.8...v3.0.0](https://github.com/runwayml/sdk-python/compare/v2.3.8...v3.0.0)

### Features

* **api:** Update with gen4_turbo, org endpoint ([#135](https://github.com/runwayml/sdk-python/issues/135)) ([7f5d1ae](https://github.com/runwayml/sdk-python/commit/7f5d1ae46c6d54576771b66abd3259641072c066))


### Chores

* **internal:** remove trailing character ([#132](https://github.com/runwayml/sdk-python/issues/132)) ([cd78e34](https://github.com/runwayml/sdk-python/commit/cd78e34930a48a8696947178ee92ae22b1210898))
* **internal:** slight transform perf improvement ([#134](https://github.com/runwayml/sdk-python/issues/134)) ([33e5a68](https://github.com/runwayml/sdk-python/commit/33e5a68198c39c04edcf055c08f43e7800f8fbc0))

## 2.3.8 (2025-03-27)

Full Changelog: [v2.3.7...v2.3.8](https://github.com/runwayml/sdk-python/compare/v2.3.7...v2.3.8)

### Chores

* fix typos ([#129](https://github.com/runwayml/sdk-python/issues/129)) ([c8047c8](https://github.com/runwayml/sdk-python/commit/c8047c87193c42b66edb7b0555c2dbc2f87b3441))

## 2.3.7 (2025-03-17)

Full Changelog: [v2.3.6...v2.3.7](https://github.com/runwayml/sdk-python/compare/v2.3.6...v2.3.7)

### Bug Fixes

* **ci:** ensure pip is always available ([#123](https://github.com/runwayml/sdk-python/issues/123)) ([e456349](https://github.com/runwayml/sdk-python/commit/e45634973c0cb9263d83ce0c1e437e65ab6c48b3))
* **ci:** remove publishing patch ([#125](https://github.com/runwayml/sdk-python/issues/125)) ([3592469](https://github.com/runwayml/sdk-python/commit/35924697f090e6198a03855d722627fc9194cdbc))

## 2.3.6 (2025-03-15)

Full Changelog: [v2.3.5...v2.3.6](https://github.com/runwayml/sdk-python/compare/v2.3.5...v2.3.6)

### Bug Fixes

* **types:** handle more discriminated union shapes ([#121](https://github.com/runwayml/sdk-python/issues/121)) ([51f8b42](https://github.com/runwayml/sdk-python/commit/51f8b42cf1efcb6294292d4a0b68522622ab95cd))


### Chores

* **internal:** bump rye to 0.44.0 ([#120](https://github.com/runwayml/sdk-python/issues/120)) ([ea18df4](https://github.com/runwayml/sdk-python/commit/ea18df47d97d7d085562eb8fa1b2406cd75c264c))
* **internal:** codegen related update ([#119](https://github.com/runwayml/sdk-python/issues/119)) ([e72357e](https://github.com/runwayml/sdk-python/commit/e72357e9013730819d973a3efa128cd232574ebd))
* **internal:** remove extra empty newlines ([#117](https://github.com/runwayml/sdk-python/issues/117)) ([4f0e93e](https://github.com/runwayml/sdk-python/commit/4f0e93e5741d2dc0a96c4e211dc74d1d272a2126))

## 2.3.5 (2025-03-11)

Full Changelog: [v2.3.4...v2.3.5](https://github.com/runwayml/sdk-python/compare/v2.3.4...v2.3.5)

## 2.3.4 (2025-03-04)

Full Changelog: [v2.3.3...v2.3.4](https://github.com/runwayml/sdk-python/compare/v2.3.3...v2.3.4)

### Chores

* **internal:** remove unused http client options forwarding ([#111](https://github.com/runwayml/sdk-python/issues/111)) ([c0fa5a9](https://github.com/runwayml/sdk-python/commit/c0fa5a92d45c82402c68556772d93d9b3f1c6de4))

## 2.3.3 (2025-02-28)

Full Changelog: [v2.3.2...v2.3.3](https://github.com/runwayml/sdk-python/compare/v2.3.2...v2.3.3)

### Chores

* **docs:** update client docstring ([#108](https://github.com/runwayml/sdk-python/issues/108)) ([3a6daf5](https://github.com/runwayml/sdk-python/commit/3a6daf52930e1875271ccacea66406081c9ac7b3))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#107](https://github.com/runwayml/sdk-python/issues/107)) ([efae113](https://github.com/runwayml/sdk-python/commit/efae1131f35849a3ff3d726a7fa80f96abb6f5d5))

## 2.3.2 (2025-02-26)

Full Changelog: [v2.3.1...v2.3.2](https://github.com/runwayml/sdk-python/compare/v2.3.1...v2.3.2)

### Chores

* **internal:** properly set __pydantic_private__ ([#104](https://github.com/runwayml/sdk-python/issues/104)) ([2d7a59f](https://github.com/runwayml/sdk-python/commit/2d7a59f3fe37823974688fea161d7b663e227475))

## 2.3.1 (2025-02-22)

Full Changelog: [v2.3.0...v2.3.1](https://github.com/runwayml/sdk-python/compare/v2.3.0...v2.3.1)

### Chores

* **internal:** fix devcontainers setup ([#101](https://github.com/runwayml/sdk-python/issues/101)) ([7a01b9a](https://github.com/runwayml/sdk-python/commit/7a01b9a9bc5576849475d3e4381312781dae4437))

## 2.3.0 (2025-02-21)

Full Changelog: [v2.2.2...v2.3.0](https://github.com/runwayml/sdk-python/compare/v2.2.2...v2.3.0)

### Features

* **client:** allow passing `NotGiven` for body ([#98](https://github.com/runwayml/sdk-python/issues/98)) ([fda401a](https://github.com/runwayml/sdk-python/commit/fda401a98a454b01de764269afb32492a38494d6))


### Bug Fixes

* **client:** mark some request bodies as optional ([fda401a](https://github.com/runwayml/sdk-python/commit/fda401a98a454b01de764269afb32492a38494d6))

## 2.2.2 (2025-02-14)

Full Changelog: [v2.2.1...v2.2.2](https://github.com/runwayml/sdk-python/compare/v2.2.1...v2.2.2)

### Bug Fixes

* asyncify on non-asyncio runtimes ([#96](https://github.com/runwayml/sdk-python/issues/96)) ([c478bc7](https://github.com/runwayml/sdk-python/commit/c478bc7b5115c637a31cb7a0a60a35265500120a))


### Chores

* **internal:** update client tests ([#94](https://github.com/runwayml/sdk-python/issues/94)) ([d8892cd](https://github.com/runwayml/sdk-python/commit/d8892cd6e439347c04fb7ba1e97abb421803f379))

## 2.2.1 (2025-02-07)

Full Changelog: [v2.2.0...v2.2.1](https://github.com/runwayml/sdk-python/compare/v2.2.0...v2.2.1)

### Chores

* **internal:** fix type traversing dictionary params ([#90](https://github.com/runwayml/sdk-python/issues/90)) ([49d44b9](https://github.com/runwayml/sdk-python/commit/49d44b9b3f234f9aa5c69e3694f1774a8a0a4581))
* **internal:** minor type handling changes ([#92](https://github.com/runwayml/sdk-python/issues/92)) ([f4f122f](https://github.com/runwayml/sdk-python/commit/f4f122f97e7bd10d51250bdcca67f55cb8a76e4a))

## 2.2.0 (2025-02-06)

Full Changelog: [v2.1.11...v2.2.0](https://github.com/runwayml/sdk-python/compare/v2.1.11...v2.2.0)

### Features

* **client:** send `X-Stainless-Read-Timeout` header ([#87](https://github.com/runwayml/sdk-python/issues/87)) ([43e6f00](https://github.com/runwayml/sdk-python/commit/43e6f005f611ddc87a11d4f7244c883a25a5c8ed))

## 2.1.11 (2025-02-04)

Full Changelog: [v2.1.10...v2.1.11](https://github.com/runwayml/sdk-python/compare/v2.1.10...v2.1.11)

### Chores

* **internal:** bummp ruff dependency ([#83](https://github.com/runwayml/sdk-python/issues/83)) ([3d1be9d](https://github.com/runwayml/sdk-python/commit/3d1be9d17d6f1bc737cf416c08cc9710aa61c94b))
* **internal:** change default timeout to an int ([#82](https://github.com/runwayml/sdk-python/issues/82)) ([38e5767](https://github.com/runwayml/sdk-python/commit/38e5767b267c108c8ef03b0fdb2508b20f74e018))

## 2.1.10 (2025-01-24)

Full Changelog: [v2.1.9...v2.1.10](https://github.com/runwayml/sdk-python/compare/v2.1.9...v2.1.10)

### Chores

* **internal:** minor formatting changes ([#80](https://github.com/runwayml/sdk-python/issues/80)) ([067f47a](https://github.com/runwayml/sdk-python/commit/067f47a1a59f15c71018bb28f3606832f223b42f))
* **internal:** minor style changes ([#78](https://github.com/runwayml/sdk-python/issues/78)) ([bd0eb4a](https://github.com/runwayml/sdk-python/commit/bd0eb4a84756ca8e8cf40935513358eac470d750))

## 2.1.9 (2025-01-21)

Full Changelog: [v2.1.8...v2.1.9](https://github.com/runwayml/sdk-python/compare/v2.1.8...v2.1.9)

### Bug Fixes

* add back missing docstrings ([#73](https://github.com/runwayml/sdk-python/issues/73)) ([8eac71e](https://github.com/runwayml/sdk-python/commit/8eac71e781ff81d00129ea224863a20bb70f00f6))
* **client:** only call .close() when needed ([#69](https://github.com/runwayml/sdk-python/issues/69)) ([4a48c73](https://github.com/runwayml/sdk-python/commit/4a48c73760d38c1f22aa73cc79f3eb1bc497e1c5))
* correctly handle deserialising `cls` fields ([#71](https://github.com/runwayml/sdk-python/issues/71)) ([6db1a75](https://github.com/runwayml/sdk-python/commit/6db1a751d3be4f8905bfed74c99b2423acfcd003))
* **tests:** make test_get_platform less flaky ([#75](https://github.com/runwayml/sdk-python/issues/75)) ([7199a24](https://github.com/runwayml/sdk-python/commit/7199a24ae13750d56648d5f4a7a2a6a2ad3ea9c4))


### Chores

* **internal:** avoid pytest-asyncio deprecation warning ([#76](https://github.com/runwayml/sdk-python/issues/76)) ([bff6464](https://github.com/runwayml/sdk-python/commit/bff646451b0b116acd763ff7d2432a9cd921fa2f))
* **internal:** codegen related update ([#67](https://github.com/runwayml/sdk-python/issues/67)) ([027aa11](https://github.com/runwayml/sdk-python/commit/027aa11dabfccf461fb33aab458a50d96d715ff9))
* **internal:** codegen related update ([#70](https://github.com/runwayml/sdk-python/issues/70)) ([38c71dc](https://github.com/runwayml/sdk-python/commit/38c71dc74ab8028b109a51266edac077549aea0b))
* **internal:** codegen related update ([#72](https://github.com/runwayml/sdk-python/issues/72)) ([d4b14b4](https://github.com/runwayml/sdk-python/commit/d4b14b4a6dfecb7f5edc18442f8326213c63db40))


### Documentation

* **raw responses:** fix duplicate `the` ([#74](https://github.com/runwayml/sdk-python/issues/74)) ([0d563ee](https://github.com/runwayml/sdk-python/commit/0d563ee146cef940d78a026302229f3949c034fc))

## 2.1.8 (2025-01-08)

Full Changelog: [v2.1.7...v2.1.8](https://github.com/runwayml/sdk-python/compare/v2.1.7...v2.1.8)

### Chores

* add missing isclass check ([#64](https://github.com/runwayml/sdk-python/issues/64)) ([a90a201](https://github.com/runwayml/sdk-python/commit/a90a201eaecb4a70714a02d270281c1f4815876d))

## 2.1.7 (2025-01-02)

Full Changelog: [v2.1.6...v2.1.7](https://github.com/runwayml/sdk-python/compare/v2.1.6...v2.1.7)

### Chores

* **internal:** codegen related update ([#61](https://github.com/runwayml/sdk-python/issues/61)) ([6248aa2](https://github.com/runwayml/sdk-python/commit/6248aa2e561cecddc440e8cdfe0773ce0353e25b))

## 2.1.6 (2024-12-18)

Full Changelog: [v2.1.5...v2.1.6](https://github.com/runwayml/sdk-python/compare/v2.1.5...v2.1.6)

### Chores

* **internal:** codegen related update ([#48](https://github.com/runwayml/sdk-python/issues/48)) ([f999274](https://github.com/runwayml/sdk-python/commit/f999274cbc241f063e3f6abdd7bef93749066c05))
* **internal:** codegen related update ([#50](https://github.com/runwayml/sdk-python/issues/50)) ([187e174](https://github.com/runwayml/sdk-python/commit/187e1747d62dc99718de5d2dfb5bc8fa8291ab34))
* **internal:** codegen related update ([#51](https://github.com/runwayml/sdk-python/issues/51)) ([1c70164](https://github.com/runwayml/sdk-python/commit/1c701642c7797d49ce59bc938b0f18511f3c6d9e))
* **internal:** codegen related update ([#52](https://github.com/runwayml/sdk-python/issues/52)) ([07e7dda](https://github.com/runwayml/sdk-python/commit/07e7ddaae96eb26063a88e6bc23adef2f9b0e7d5))
* **internal:** codegen related update ([#54](https://github.com/runwayml/sdk-python/issues/54)) ([5540248](https://github.com/runwayml/sdk-python/commit/55402489160f4cb43244f90e5f85c90bd96a7729))
* **internal:** codegen related update ([#55](https://github.com/runwayml/sdk-python/issues/55)) ([75daba1](https://github.com/runwayml/sdk-python/commit/75daba1936f201824daec2b8b08abf68a52b55d7))
* **internal:** codegen related update ([#56](https://github.com/runwayml/sdk-python/issues/56)) ([c98ed80](https://github.com/runwayml/sdk-python/commit/c98ed80958344be95507a3c5ef7ede3006cf6bf5))
* **internal:** fix some typos ([#58](https://github.com/runwayml/sdk-python/issues/58)) ([404c771](https://github.com/runwayml/sdk-python/commit/404c771242c581f9c618966a03b5de5f5db8a5da))


### Documentation

* **readme:** example snippet for client context manager ([#57](https://github.com/runwayml/sdk-python/issues/57)) ([e62b5e9](https://github.com/runwayml/sdk-python/commit/e62b5e9d1176d72c7285ede6200436bc994260ae))

## 2.1.5 (2024-12-13)

Full Changelog: [v2.1.4...v2.1.5](https://github.com/runwayml/sdk-python/compare/v2.1.4...v2.1.5)

### Chores

* **internal:** add support for TypeAliasType ([#46](https://github.com/runwayml/sdk-python/issues/46)) ([278afad](https://github.com/runwayml/sdk-python/commit/278afade7c0541db8a14f4dbb763ec6cd2797558))
* **internal:** bump pyright ([#44](https://github.com/runwayml/sdk-python/issues/44)) ([eb51ffa](https://github.com/runwayml/sdk-python/commit/eb51ffa9ef89567501d19cf9183ac64792062559))

## 2.1.4 (2024-12-10)

Full Changelog: [v2.1.3...v2.1.4](https://github.com/runwayml/sdk-python/compare/v2.1.3...v2.1.4)

### Chores

* **internal:** bump pydantic dependency ([#40](https://github.com/runwayml/sdk-python/issues/40)) ([ae3a845](https://github.com/runwayml/sdk-python/commit/ae3a8457855179ccc6e784e2e2cf39613fedddcd))


### Documentation

* **readme:** fix http client proxies example ([#42](https://github.com/runwayml/sdk-python/issues/42)) ([d1389f7](https://github.com/runwayml/sdk-python/commit/d1389f73504fc60d07be4742ea12c7f9d5841034))

## 2.1.3 (2024-12-04)

Full Changelog: [v2.1.2...v2.1.3](https://github.com/runwayml/sdk-python/compare/v2.1.2...v2.1.3)

### Chores

* make the `Omit` type public ([#35](https://github.com/runwayml/sdk-python/issues/35)) ([a333528](https://github.com/runwayml/sdk-python/commit/a3335281c52a8f6e6a85f98623c48e228245fa04))

## 2.1.2 (2024-12-03)

Full Changelog: [v2.1.1...v2.1.2](https://github.com/runwayml/sdk-python/compare/v2.1.1...v2.1.2)

### Chores

* **internal:** bump pyright ([#32](https://github.com/runwayml/sdk-python/issues/32)) ([7d36972](https://github.com/runwayml/sdk-python/commit/7d36972a3afa9335141b848cb9783c649a4933ae))

## 2.1.1 (2024-11-28)

Full Changelog: [v2.1.0...v2.1.1](https://github.com/runwayml/sdk-python/compare/v2.1.0...v2.1.1)

### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#28](https://github.com/runwayml/sdk-python/issues/28)) ([f5e637e](https://github.com/runwayml/sdk-python/commit/f5e637eb373bc6fa85ca6d123bbdaaa1161bc814))


### Chores

* **internal:** exclude mypy from running on tests ([#27](https://github.com/runwayml/sdk-python/issues/27)) ([d724387](https://github.com/runwayml/sdk-python/commit/d724387c6546ba476e2773f2249475285dca32c9))
* **internal:** fix compat model_dump method when warnings are passed ([#24](https://github.com/runwayml/sdk-python/issues/24)) ([61c8490](https://github.com/runwayml/sdk-python/commit/61c849057b971f8b19846ed08b5145c4321adf04))
* rebuild project due to codegen change ([#19](https://github.com/runwayml/sdk-python/issues/19)) ([2a4cf56](https://github.com/runwayml/sdk-python/commit/2a4cf56335868d88e07aac767260c0c7509b1c94))
* rebuild project due to codegen change ([#21](https://github.com/runwayml/sdk-python/issues/21)) ([e680d5b](https://github.com/runwayml/sdk-python/commit/e680d5b5bf3ee7fcdede74c7d5c5a971ea18675e))
* rebuild project due to codegen change ([#22](https://github.com/runwayml/sdk-python/issues/22)) ([ecddf51](https://github.com/runwayml/sdk-python/commit/ecddf51a41704e42f2612541d3841990f22f7220))
* remove now unused `cached-property` dep ([#26](https://github.com/runwayml/sdk-python/issues/26)) ([21e64d0](https://github.com/runwayml/sdk-python/commit/21e64d0603003c58918dde0b5b6e94b7df28707c))


### Documentation

* add info log level to readme ([#25](https://github.com/runwayml/sdk-python/issues/25)) ([d6e4ed4](https://github.com/runwayml/sdk-python/commit/d6e4ed45841a88e13c30dd318706a18bf86a8550))

## 2.1.0 (2024-11-06)

Full Changelog: [v2.0.0...v2.1.0](https://github.com/runwayml/sdk-python/compare/v2.0.0...v2.1.0)

### Features

* **api:** API version 2024-11-06 ([#15](https://github.com/runwayml/sdk-python/issues/15)) ([39c096f](https://github.com/runwayml/sdk-python/commit/39c096fdc4784cc726e8688dcc3263e6cb322607))
* **api:** Set latest default API version ([#17](https://github.com/runwayml/sdk-python/issues/17)) ([2ad66fd](https://github.com/runwayml/sdk-python/commit/2ad66fd753321eaae28fa09755bfdb6bbfc07949))

## 2.0.0 (2024-10-04)

Full Changelog: [v1.0.0...v2.0.0](https://github.com/runwayml/sdk-python/compare/v1.0.0...v2.0.0)

### Features

* **api:** update via SDK Studio ([#7](https://github.com/runwayml/sdk-python/issues/7)) ([e31ea2c](https://github.com/runwayml/sdk-python/commit/e31ea2ca5602245bd936d564b66752f592cc2fab))


### Chores

* **internal:** codegen related update ([#10](https://github.com/runwayml/sdk-python/issues/10)) ([b1b5a5f](https://github.com/runwayml/sdk-python/commit/b1b5a5f1eb6dadc9674e771a598d7269a6ed23b2))
* **internal:** codegen related update ([#11](https://github.com/runwayml/sdk-python/issues/11)) ([6a8ccd0](https://github.com/runwayml/sdk-python/commit/6a8ccd00924f775851a9a8e9429ae4b2f1790dee))
* **internal:** codegen related update ([#8](https://github.com/runwayml/sdk-python/issues/8)) ([c66ad91](https://github.com/runwayml/sdk-python/commit/c66ad91471c094e4c42bbbefdce4ea0d81fe487f))

## 1.0.0 (2024-09-18)

Full Changelog: [v0.1.0-alpha.1...v1.0.0](https://github.com/runwayml/sdk-python/compare/v0.1.0-alpha.1...v1.0.0)

### Chores

* update SDK settings ([#4](https://github.com/runwayml/sdk-python/issues/4)) ([50c8fb7](https://github.com/runwayml/sdk-python/commit/50c8fb734438fc6a969d8d3acbe9134fa08ff839))

## 0.1.0-alpha.1 (2024-09-16)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/runwayml/sdk-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([d2b36be](https://github.com/runwayml/sdk-python/commit/d2b36bedb109763c0ff0bccdde9d3fcc52702276))
* **api:** update via SDK Studio ([458cea2](https://github.com/runwayml/sdk-python/commit/458cea250a60c3e3985bdb5e0844e0df8609bbd1))
* **api:** update via SDK Studio ([8218b59](https://github.com/runwayml/sdk-python/commit/8218b596c6fabcceec835538351c117f0969d707))


### Chores

* go live ([#1](https://github.com/runwayml/sdk-python/issues/1)) ([9de5b2d](https://github.com/runwayml/sdk-python/commit/9de5b2d9e40235caf22a1449f5da746f51130a3b))
* **internal:** bump pyright / mypy version ([329a9ff](https://github.com/runwayml/sdk-python/commit/329a9ffbd815ee81c1f7159ac26c8afef5b65402))
* **internal:** bump ruff ([8152032](https://github.com/runwayml/sdk-python/commit/815203243e2012e19786ea8d7dc333747b68215e))
* **internal:** codegen related update ([05e04a7](https://github.com/runwayml/sdk-python/commit/05e04a7f3f996bdf4152de3c57feabd2c36e7f45))
* **internal:** codegen related update ([a6d2ae7](https://github.com/runwayml/sdk-python/commit/a6d2ae7a04d17f1f75fbb4eae6a516c78fe2e6fc))


### Documentation

* update CONTRIBUTING.md ([3fd55c0](https://github.com/runwayml/sdk-python/commit/3fd55c0187956375a9da938cb6c757c30f0a3789))
