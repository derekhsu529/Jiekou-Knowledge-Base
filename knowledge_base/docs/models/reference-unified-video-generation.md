---
title: "视频生成通用接口"
url: "https://docs.jiekou.ai/docs/models/reference-unified-video-generation.md"
crawled_at: "2026-02-26T23:35:22.451724"
---

Published Time: Thu, 26 Feb 2026 15:35:22 GMT

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.jiekou.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 视频生成通用接口

export const UnifiedAPI = () => {
  if (typeof document === "undefined") {
    return null;
  }
  const [config, setConfig] = useState(window.jiekouRemoteData?.videoUnifyAPIConfig?.data || null);
  const [chosenIndex, setChosenIndex] = useState(0);
  const [isOpen, setIsOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [searchTerm, setSearchTerm] = useState("");
  useEffect(() => {
    if (!window.jiekouRemoteData?.videoUnifyAPIConfig?.data) {
      setIsLoading(true);
      fetch('https://api.jiekou.ai/v3/admin/video-unify-api/config').then(response => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      }).then(data => {
        setConfig(data.configs);
      }).catch(error => {
        console.error('Failed to fetch config:', error);
      }).finally(() => {
        setIsLoading(false);
      });
    }
  }, []);
  const data = useMemo(() => {
    return config?.[chosenIndex];
  }, [config, chosenIndex]);
  useEffect(() => {
    const handleClickOutside = event => {
      if (isOpen && !event.target.closest(".unified-api-selector-container")) {
        setIsOpen(false);
        setSearchTerm("");
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [isOpen]);
  const filteredConfig = useMemo(() => {
    if (!config || !searchTerm.trim()) {
      return config || [];
    }
    const term = searchTerm.toLowerCase();
    return config.filter(item => {
      const model = (item.model || '').toLowerCase();
      const description = (item.description || '').toLowerCase();
      return model.includes(term) || description.includes(term);
    });
  }, [config, searchTerm]);
  const modelSelector = useMemo(() => {
    if (!config || config.length <= 1) {
      return null;
    }
    const selectedModel = config[chosenIndex]?.model || '-';
    return 

 选择要使用的模型  

  setIsOpen(!isOpen)} className="unified-api-selector-button"> {selectedModel}   {isOpen && 

 

  setSearchTerm(e.target.value)} className="unified-api-search-input" onClick={e => e.stopPropagation()} /> 

 

 {filteredConfig.length > 0 ? filteredConfig.map((item, filteredIndex) => { const originalIndex = config.findIndex(configItem => configItem === item); return 

 { setChosenIndex(originalIndex); setIsOpen(false); setSearchTerm(""); }} className={`unified-api-selector-option ${originalIndex === chosenIndex ? "selected" : ""}`}> {item.model || '-'} 

; }) : 

 没有找到匹配的模型 

} 

 

} 

 

;
  }, [config, chosenIndex, isOpen, searchTerm, filteredConfig]);
  const headerFields = useMemo(() => {
    return <>
        
请求头
---

         枚举值: application/json 
         Bearer 身份验证格式: Bearer {`{{API 秘钥}}`}。 
      </>;
  }, []);
  const requestBodyFields = useMemo(() => {
    if (!data?.json_schema) {
      return null;
    }
    const schema = JSON.parse(data.json_schema);
    const getFields = () => {
      return Object.entries(schema.properties).filter(([key, value]) => key !== "model").map(([key, value]) => ({
        name: key,
        ...value
      }));
    };
    const getFieldInfo = fieldName => {
      const field = schema.properties[fieldName];
      if (!field) return {
        type: "string",
        required: false
      };
      return {
        type: field.type || "string",
        required: schema.required?.includes(fieldName) || false,
        description: field.description,
        enum: field.enum,
        default: field.default,
        minLength: field.minLength,
        maxLength: field.maxLength,
        minimum: field.minimum,
        maximum: field.maximum,
        maxItems: field.maxItems,
        items: field.items
      };
    };
    const renderFieldConstraints = fieldInfo => {
      return <>
          {fieldInfo.maxItems !== undefined && 
最大支持项数:{" "}  {fieldInfo.maxItems}

}
          {(fieldInfo.minLength || fieldInfo.maxLength) && 
{fieldInfo.minLength !== undefined && <> 最小长度:{" "}  {fieldInfo.minLength}  </>} {fieldInfo.minLength !== undefined && fieldInfo.maxLength && "，"} {fieldInfo.maxLength && <> 最大长度:{" "}  {fieldInfo.maxLength}  </>} 。

}
          {(fieldInfo.minimum !== undefined || fieldInfo.maximum !== undefined) && 
{fieldInfo.minimum !== undefined && <> 最小值:{" "}  {fieldInfo.minimum}  </>} {fieldInfo.minimum !== undefined && fieldInfo.maximum !== undefined && "，"} {fieldInfo.maximum !== undefined && <> 最大值:{" "}  {fieldInfo.maximum}  </>} 。

}
          {(fieldInfo.enum || fieldInfo.default !== undefined) && 
{fieldInfo.enum && <> 枚举值:{" "} {fieldInfo.enum.map((value, index) =>   {value}  {index < fieldInfo.enum.length - 1 && ", "} )} </>} {fieldInfo.enum && fieldInfo.default !== undefined && "。 "} {fieldInfo.default !== undefined && <> 默认值:{" "}  {typeof fieldInfo.default === 'boolean' ? fieldInfo.default ? 'true' : 'false' : fieldInfo.default}  </>} 。

}
        </>;
    };
    return <>
        {data?.model &&  支持的模型： {data.model} }
        {getFields().map(field => {
      const fieldInfo = getFieldInfo(field.name);
      return  
{fieldInfo.description}

 {renderFieldConstraints(fieldInfo)} {fieldInfo.items && fieldInfo.items.properties &&  {Object.entries(fieldInfo.items.properties).map(([propName, propInfo]) =>  
{propInfo.description}

 {renderFieldConstraints(propInfo)} )} } ;
    })}
      </>;
  }, [data]);
  const LoadingSpinner = useMemo(() => 

  
加载中...

 

, []);
  return 

 
该接口用于统一整合各厂商的视频生成功能，抽取通用的请求与响应字段，规范参数和数据格式，简化调用流程，提高接入与使用效率。

 {modelSelector} {data?.description && <> 
模型信息：

 
{data.description}

 </>} {headerFields} 
请求体
---

 {isLoading ? LoadingSpinner : requestBodyFields} 
返回结果
----

  异步任务的 task_id。您应该使用该 task_id 请求{" "} [查询任务结果 API](https://docs.jiekou.ai/docs/models/reference-get-async-task-result){" "} 以获取生成结果  

;
};
