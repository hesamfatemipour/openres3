local http = require "socket.http"
local ngx = require "ngx"

_MIDDLEWARE = {}

MIDDLEWARE_HOST = "http://10.0.1.12"
MIDDLEWARE_PORT = "5000"

function _MIDDLEWARE.talk_to_middleware(user_id, bucket_name)
-- communicate with middleware to validate the requested bucket name
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

-- this is a mocked version of the api
function _MIDDLEWARE.send_request_to_storage(user_id, bucket_name)
    -- send request to arvan S3
        local url = string.format("https://") -- create bucket api's url

        local result, resp_status_code, resp_headers, resp_status = http.request {
        body = headers = {
            ["user_id"] = user_id,
            ["bucket_name"] = bucket_name,
        },
        method = "POST",
        url = url,
        headers = {
            ["Content-Type"] = "text/plain",
        },
    }
end

return _MIDDLEWARE