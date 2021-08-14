@echo off
@del config.json
@echo QQ account:
@set /p input=
@set uid=%input%
@echo QQ password:
@set /p input=
@set upass=%input%
@echo enable http?(Y/n)
@set /p input=
@set http=true
if "%input%" == "n" ( set http=false )
if "%input%" == "N" ( set http=false)
@echo enable ws?(Y/n)
@set /p input=
@set ws=true
if "%input%" == "n" ( set ws=false )
if "%input%" == "N" ( set ws=false )
@echo { >>config.json
@echo 	"uin": %uid%, >>config.json
@echo 	"password": "%upass%", >>config.json
@echo 	"encrypt_password": false, >>config.json
@echo 	"password_encrypted": "", >>config.json
@echo 	"enable_db": true, >>config.json
@echo 	"access_token": "", >>config.json
@echo 	"relogin": { >>config.json
@echo 		"enabled": true, >>config.json
@echo 		"relogin_delay": 3, >>config.json
@echo 		"max_relogin_times": 0 >>config.json
@echo 	}, >>config.json
@echo 	"_rate_limit": { >>config.json
@echo 		"enabled": false, >>config.json
@echo 		"frequency": 1, >>config.json
@echo 		"bucket_size": 1 >>config.json
@echo 	}, >>config.json
@echo 	"ignore_invalid_cqcode": false, >>config.json
@echo 	"force_fragmented": true, >>config.json
@echo 	"heartbeat_interval": 0, >>config.json
@echo 	"http_config": { >>config.json
@echo 		"enabled": %http%, >>config.json
@echo 		"host": "0.0.0.0", >>config.json
@echo 		"port": 5700, >>config.json
@echo 		"timeout": 0, >>config.json
@echo 		"post_urls": {} >>config.json
@echo 	}, >>config.json
@echo 	"ws_config": { >>config.json
@echo 		"enabled": %ws%, >>config.json
@echo 		"host": "0.0.0.0", >>config.json
@echo 		"port": 6700 >>config.json
@echo 	}, >>config.json
@echo 	"ws_reverse_servers": [ >>config.json
@echo 		{ >>config.json
@echo 			"enabled": false, >>config.json
@echo 			"reverse_url": "ws://you_websocket_universal.server", >>config.json
@echo 			"reverse_api_url": "ws://you_websocket_api.server", >>config.json
@echo 			"reverse_event_url": "ws://you_websocket_event.server", >>config.json
@echo 			"reverse_reconnect_interval": 3000 >>config.json
@echo 		} >>config.json
@echo 	], >>config.json
@echo 	"post_message_format": "string", >>config.json
@echo 	"debug": false, >>config.json
@echo 	"log_level": "" >>config.json
@echo } >>config.json
@pause
