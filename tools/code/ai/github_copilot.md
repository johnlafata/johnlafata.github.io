# I installed the github copilot extension.
### TODO add support for java and python
https://code.visualstudio.com/docs/languages/identifiers

A free trial of Github copilot is available but requires a subscription. 

I opted to install the extension and will evaluate it for a while before deciding whether to subscribe.

However after enabling the extension and subscribing to copilot on github, I found that it requested more access to my github account. 
```
This application will be able to read and write all public and private repository data. This includes the following:
* Code
* Issues
* Pull requests
* * Wikis
* Settings
* Webhooks and services
* Deploy keys
* Collaboration invites
Note: In addition to repository related resources, the repo scope also grants access to manage organization attributes and organization-owned resources including projects, invitations, team memberships and webhooks. This scope also grants the ability to manage projects owned by users.
```
I'm not sure if I want to give it access to both my public and private repos and  organizations that I am only a member of).  I'll have to think about this - so I just didn't git it access to my github account for now.

# I also installed the open copilot extension. 
AI Copilot powered by self-hosted llama.cpp endpoint.
It uses llama.cpp which I didn't install but want to experiment with. Still thinking whether I want to use the a self-hosted llama or use github copilot. 
https://github.com/ggerganov/llama.cpp
####  I installed llama.cpp from the following instructions
https://github.com/ggerganov/llama.cpp/blob/master/docs/install.md

```bash
brew install llama.cpp
```

then I cloned the git repo to get the model files
```bash
cd ~/reference-workspace
git clone git@github.com:ggerganov/llama.cpp.git
cd ~/personal-workspace
export LLAMA_CPP_HOME=~/reference-workspace/llama.cpp
echo $LLAMA_CPP_HOME
ls ${LLAMA_CPP_HOME}/models/*.gguf
```

##### these did not work - and I'm not 100% sure why - so more research needed on how to use a local model
```bash
llama-cli -m ${LLAMA_CPP_HOME}/models/ggml-vocab-starcoder
```
```
llama-server -m ${LLAMA_CPP_HOME}/models/ggml-vocab-starcoder.gguf
```

##### this worked, it downloaded the startcoder model from hugging face, I'm waiting for it to work
see this reference: https://huggingface.co/osukhoroslov-hw/starcoder-Q5_K_M-GGUF
```
llama-server --hf-repo osukhoroslov-hw/starcoder-Q5_K_M-GGUF --hf-file starcoder-q5_k_m.gguf -c 2048
```
results:
```bash
build: 3892 (96b69121) with Apple clang version 15.0.0 (clang-1500.3.9.4) for arm64-apple-darwin23.4.0
system info: n_threads = 12, n_threads_batch = 12, total_threads = 16

system_info: n_threads = 12 (n_threads_batch = 12) / 16 | AVX = 0 | AVX_VNNI = 0 | AVX2 = 0 | AVX512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | AVX512_BF16 = 0 | FMA = 0 | NEON = 1 | SVE = 0 | ARM_FMA = 1 | F16C = 0 | FP16_VA = 1 | RISCV_VECT = 0 | WASM_SIMD = 0 | BLAS = 1 | SSE3 = 0 | SSSE3 = 0 | VSX = 0 | MATMUL_INT8 = 1 | LLAMAFILE = 1 | 

main: HTTP server is listening, hostname: 127.0.0.1, port: 8080, http threads: 15
main: loading model
llama_download_file: no previous model file found /Users/johnlafata/Library/Caches/llama.cpp/starcoder-q5_k_m.gguf
curl_perform_with_retry: Trying to download from https://huggingface.co/osukhoroslov-hw/starcoder-Q5_K_M-GGUF/resolve/main/starcoder-q5_k_m.gguf (attempt 1 of 3)...
llama_download_file: trying to download model from https://huggingface.co/osukhoroslov-hw/starcoder-Q5_K_M-GGUF/resolve/main/starcoder-q5_k_m.gguf to /Users/johnlafata/Library/Caches/llama.cpp/starcoder-q5_k_m.gguf (server_etag:"f7e3e31e7e24c999872a4e48746804b9-732", server_last_modified:Fri, 12 Jul 2024 17:55:58 GMT)...
curl_perform_with_retry: Trying to download from https://huggingface.co/osukhoroslov-hw/starcoder-Q5_K_M-GGUF/resolve/main/starcoder-q5_k_m.gguf (attempt 1 of 3)...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1116  100  1116    0     0  21521      0 --:--:-- --:--:-- --:--:-- 21521
100 10.8G  100 10.8G    0     0  14.1M      0  0:13:11  0:13:11 --:--:-- 15.6M
llama_download_file: file metadata saved: /Users/johnlafata/Library/Caches/llama.cpp/starcoder-q5_k_m.gguf.json
llama_model_loader: loaded meta data with 19 key-value pairs and 485 tensors from /Users/johnlafata/Library/Caches/llama.cpp/starcoder-q5_k_m.gguf (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = starcoder
llama_model_loader: - kv   1:                               general.name str              = StarCoder
llama_model_loader: - kv   2:                   starcoder.context_length u32              = 8192
llama_model_loader: - kv   3:                 starcoder.embedding_length u32              = 6144
llama_model_loader: - kv   4:              starcoder.feed_forward_length u32              = 24576
llama_model_loader: - kv   5:                      starcoder.block_count u32              = 40
llama_model_loader: - kv   6:             starcoder.attention.head_count u32              = 48
llama_model_loader: - kv   7:          starcoder.attention.head_count_kv u32              = 1
llama_model_loader: - kv   8:     starcoder.attention.layer_norm_epsilon f32              = 0.000010
llama_model_loader: - kv   9:                          general.file_type u32              = 17
llama_model_loader: - kv  10:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  11:                         tokenizer.ggml.pre str              = refact
llama_model_loader: - kv  12:                      tokenizer.ggml.tokens arr[str,49152]   = ["<|endoftext|>", "<fim_prefix>", "<f...
llama_model_loader: - kv  13:                  tokenizer.ggml.token_type arr[i32,49152]   = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, ...
llama_model_loader: - kv  14:                      tokenizer.ggml.merges arr[str,48891]   = ["Ġ Ġ", "ĠĠ ĠĠ", "ĠĠĠĠ ĠĠ...
llama_model_loader: - kv  15:                tokenizer.ggml.bos_token_id u32              = 0
llama_model_loader: - kv  16:                tokenizer.ggml.eos_token_id u32              = 0
llama_model_loader: - kv  17:            tokenizer.ggml.unknown_token_id u32              = 0
llama_model_loader: - kv  18:               general.quantization_version u32              = 2
llama_model_loader: - type  f32:  323 tensors
llama_model_loader: - type q5_K:  101 tensors
llama_model_loader: - type q6_K:   61 tensors
llm_load_vocab: special tokens cache size = 19
llm_load_vocab: token to piece cache size = 0.2826 MB
llm_load_print_meta: format           = GGUF V3 (latest)
llm_load_print_meta: arch             = starcoder
llm_load_print_meta: vocab type       = BPE
llm_load_print_meta: n_vocab          = 49152
llm_load_print_meta: n_merges         = 48891
llm_load_print_meta: vocab_only       = 0
llm_load_print_meta: n_ctx_train      = 8192
llm_load_print_meta: n_embd           = 6144
llm_load_print_meta: n_layer          = 40
llm_load_print_meta: n_head           = 48
llm_load_print_meta: n_head_kv        = 1
llm_load_print_meta: n_rot            = 128
llm_load_print_meta: n_swa            = 0
llm_load_print_meta: n_embd_head_k    = 128
llm_load_print_meta: n_embd_head_v    = 128
llm_load_print_meta: n_gqa            = 48
llm_load_print_meta: n_embd_k_gqa     = 128
llm_load_print_meta: n_embd_v_gqa     = 128
llm_load_print_meta: f_norm_eps       = 1.0e-05
llm_load_print_meta: f_norm_rms_eps   = 0.0e+00
llm_load_print_meta: f_clamp_kqv      = 0.0e+00
llm_load_print_meta: f_max_alibi_bias = 0.0e+00
llm_load_print_meta: f_logit_scale    = 0.0e+00
llm_load_print_meta: n_ff             = 24576
llm_load_print_meta: n_expert         = 0
llm_load_print_meta: n_expert_used    = 0
llm_load_print_meta: causal attn      = 1
llm_load_print_meta: pooling type     = 0
llm_load_print_meta: rope type        = 0
llm_load_print_meta: rope scaling     = linear
llm_load_print_meta: freq_base_train  = 10000.0
llm_load_print_meta: freq_scale_train = 1
llm_load_print_meta: n_ctx_orig_yarn  = 8192
llm_load_print_meta: rope_finetuned   = unknown
llm_load_print_meta: ssm_d_conv       = 0
llm_load_print_meta: ssm_d_inner      = 0
llm_load_print_meta: ssm_d_state      = 0
llm_load_print_meta: ssm_dt_rank      = 0
llm_load_print_meta: ssm_dt_b_c_rms   = 0
llm_load_print_meta: model type       = 15B
llm_load_print_meta: model ftype      = Q5_K - Medium
llm_load_print_meta: model params     = 15.82 B
llm_load_print_meta: model size       = 10.90 GiB (5.92 BPW) 
llm_load_print_meta: general.name     = StarCoder
llm_load_print_meta: BOS token        = 0 '<|endoftext|>'
llm_load_print_meta: EOS token        = 0 '<|endoftext|>'
llm_load_print_meta: UNK token        = 0 '<|endoftext|>'
llm_load_print_meta: LF token         = 145 'Ä'
llm_load_print_meta: EOT token        = 0 '<|endoftext|>'
llm_load_print_meta: EOG token        = 0 '<|endoftext|>'
llm_load_print_meta: max token length = 512
llm_load_tensors: ggml ctx size =    0.43 MiB
llm_load_tensors: offloading 40 repeating layers to GPU
llm_load_tensors: offloading non-repeating layers to GPU
llm_load_tensors: offloaded 41/41 layers to GPU
llm_load_tensors:      Metal buffer size = 10769.63 MiB
llm_load_tensors:        CPU buffer size =   390.00 MiB
................................................................................................
llama_new_context_with_model: n_ctx      = 2048
llama_new_context_with_model: n_batch    = 2048
llama_new_context_with_model: n_ubatch   = 512
llama_new_context_with_model: flash_attn = 0
llama_new_context_with_model: freq_base  = 10000.0
llama_new_context_with_model: freq_scale = 1
ggml_metal_init: allocating
ggml_metal_init: found device: Apple M3 Max
ggml_metal_init: picking default device: Apple M3 Max
ggml_metal_init: using embedded metal library
ggml_metal_init: GPU name:   Apple M3 Max
ggml_metal_init: GPU family: MTLGPUFamilyApple9  (1009)
ggml_metal_init: GPU family: MTLGPUFamilyCommon3 (3003)
ggml_metal_init: GPU family: MTLGPUFamilyMetal3  (5001)
ggml_metal_init: simdgroup reduction support   = true
ggml_metal_init: simdgroup matrix mul. support = true
ggml_metal_init: hasUnifiedMemory              = true
ggml_metal_init: recommendedMaxWorkingSetSize  = 38654.71 MB
llama_kv_cache_init:      Metal KV buffer size =    40.00 MiB
llama_new_context_with_model: KV self size  =   40.00 MiB, K (f16):   20.00 MiB, V (f16):   20.00 MiB
llama_new_context_with_model:        CPU  output buffer size =     0.38 MiB
llama_new_context_with_model:      Metal compute buffer size =   220.00 MiB
llama_new_context_with_model:        CPU compute buffer size =    28.01 MiB
llama_new_context_with_model: graph nodes  = 1489
llama_new_context_with_model: graph splits = 2
llama_init_from_gpt_params: warming up the model with an empty run - please wait ... (--no-warmup to disable)
srv          init: initializing slots, n_slots = 1
slot         init: id  0 | task -1 | new slot n_ctx_slot = 2048
main: model loaded
main: chat template, built_in: 1, chat_example: '<|im_start|>system
You are a helpful assistant<|im_end|>
<|im_start|>user
Hello<|im_end|>
<|im_start|>assistant
Hi there<|im_end|>
<|im_start|>user
How are you?<|im_end|>
<|im_start|>assistant
'
main: server is listening on 127.0.0.1:8080 - starting the main loop
srv  update_slots: all slots are idle
```

It took 13 minutes to download the model and launch, but the second time I ran it the model was cached so it was able to start faster.

###### I edited the settings for open copilot extension  using the ui in VS code.
http://127.0.0.1:8080

llama.cpp seems to be working now.  I had it generate a unit test for a simple test class.

As I used cody with Llama.cpp I think I encountered a limit of 1000 tokens.  I'm not sure if this is a limit of the model or the server.  I'll have to investigate further.



