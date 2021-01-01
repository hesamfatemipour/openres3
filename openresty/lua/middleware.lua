--local http = require "socket.http"
local ngx = require "ngx"

_MIDDLEWARE = {}

function _MIDDLEWARE.talk_to_middleware(user_id, bucket_name)
    local url = string.format("%s:%s/users/%s?bucket_name=%s", MIDDLEWARE_HOST, MIDDLEWARE_PORT, user_id, bucket_name)

    local result, resp_status_code, resp_headers, resp_status = http.request {
        method = "POST",
        url = url,
        headers = {
            ["Content-Type"] = "text/plain",
        },
    }
    if resp_status_code == 200 then
        can_create = true
    else
        can_create = false
    end

    return can_create
end

function _MIDDLEWARE.send_request_to_storage(secret, access_key, bucket_name)
    -- send request to arvan S3
end

return _MIDDLEWARE